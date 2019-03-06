from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
# Create your models here.

class Songs(models.Model):
	title=models.CharField(max_length=200)
	genre=models.CharField(max_length=100)
	artist=models.CharField(default='artist',max_length=100)
	song_img=models.FileField()

	class Meta:
		#gives proper plural name for admin console
		verbose_name_plural="Songs"

	def __str__(self):
		return self.title

class Ratings(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	song=models.ForeignKey(Songs,on_delete=models.CASCADE)
	rating=models.IntegerField(default=1,validators=[MaxValueValidator(5),MinValueValidator(0)])

	class Meta:
		#gives proper plural name for admin console
		verbose_name_plural="Ratings"