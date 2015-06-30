from django.db import models
from datetime import date, time


# Create your models here.
class History(models.Model):
	collect_time = models.DateTimeField(auto_now=True)
	sensor_low = models.CharField(max_length=30)
	sensor_mid = models.CharField(max_length=30)
	sensor_high = models.CharField(max_length=30)
	sensor_floor = models.CharField(max_length=30)

   
class Cleaning(models.Model):
	collect_date = models.DateTimeField(auto_now=True)
	state_of_success  = models.BooleanField()
	time_of_cleaning = models.CharField(max_length=30) 
