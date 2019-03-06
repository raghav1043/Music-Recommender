from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import Http404
from .forms import NewUserForm
from .models import Songs,Ratings
from web.recommendation import recommender
from django.db.models import Case, When
import numpy as np 
import pandas as pd

# Create your views here.

def homepage(request):
    return render(request,'web/homepage.html')

def music(request):
    song_list=Songs.objects.all()
    query=request.GET.get('q')
    if query:
        song_list=Songs.objects.filter(headline__startswith="q").all()
        return render(request,'web/music.html',{'songs': song_list})
    return render(request,'web/music.html',{'songs':song_list})

def recommendation(request):
    if not request.user.is_authenticated:
        return redirect("main:login")
    current_user_id= request.user.id
    pk_list=recommender(current_user_id)

    for i in range(0,len(pk_list)):
        id=pk_list[i]
        print(Songs.objects.get(pk=id))

    preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(pk_list)])
    song_list = Songs.objects.filter(pk__in=pk_list).order_by(preserved)
    return render(request,'web/recommendation.html',{'songs':song_list})


# register or signup
def register(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user=form.save()
			username=form.cleaned_data.get('username')
			messages.success(request, f"You are loggedin as: {username}")
			login(request,user)
			return redirect("/")

		else :
			for msg in form.error.messages :
				messages.error(request, f"{msg}: {form.error_messages[msg]}")
			return render(request = request,template_name = "web/register.html",context={"form":form})

	form=NewUserForm

	return render(request = request,template_name = "web/register.html",context={"form":form})


# logout user
def logout_request(request):
	logout(request)
	messages.info(request,"Logged out successfully")
	return redirect("main:homepage")


# login user 

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "web/login.html",
                    context={"form":form})

