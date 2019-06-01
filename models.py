from django.db import models

# Create your models here.

class Teacher(models.Model):
	first_name = models.CharField(max_length = 50)
	last_name = models.CharField(max_length = 50)
	date_of_birth = models.DateField()
	registration_number = models.CharField(max_length = 20)
	place_of_recidance = models.CharField(max_length = 20)
	phone_number = models.CharField(max_length = 16)
	email = models.EmailField(max_length = 70)
	guardian_phone = models.CharField(max_length = 16)
	id_number = models.IntegerField()
	date_employed = models.DateField()
	proffesional = models.CharField(max_length = 30)


