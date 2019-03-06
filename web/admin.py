from django.contrib import admin
from .models import Songs,Ratings
from django.db import models

# Register your models here.
class SongsAdmin(admin.ModelAdmin):
	fields=["title",
			"genre",
			"rating",]

# class MyModelAdmin(admin.ModelAdmin):
#     actions = [export_csv, export_xls, export_xlsx]

admin.site.register(Songs)
admin.site.register(Ratings)