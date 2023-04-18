from django.db import models
import datetime
from django.utils import timezone

class User(models.Model):
    GENDER_CHOICES= [
    ('M', 'Male'),
    ('F', 'Female'), 
    ('O', 'Other')
    ]
    user_id = models.AutoField(primary_key = True)
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    pwd = models.CharField(max_length = 15)
    type_of_user = models.CharField(max_length = 2)
    gender = models.CharField(max_length = 1, choices = GENDER_CHOICES)
    date_of_birth = models.DateTimeField('DOB')
    email = models.CharField(max_length = 100, unique = True)
    phone = models.CharField(max_length = 10)
    address = models.CharField(max_length = 300)

    def __str__(self):
       return str(self.user_id)

class Provider(models.Model):
    provider_id = models.OneToOneField(User, on_delete = models.CASCADE, unique=True)
    speciality = models.CharField(max_length = 100)
    hospital = models.CharField(max_length  = 100)

class Patient(models.Model):
    BLOOD_GROUPS= [
    ('A+', 'A+'),
    ('A-', 'A-'), 
    ('B+', 'B+'),
    ('B-', 'B-'),
    ('O+', 'O+'),
    ('O-', 'O-'),
    ('AB+', 'AB+'),
    ('AB-', 'AB-'),
    ]
    patient_id = models.OneToOneField(User, on_delete = models.CASCADE, unique=True)
    doctor_id = models.CharField(max_length = 300)
    hospital = models.CharField(max_length = 300)
    blood_group = models.CharField(max_length = 5, choices = BLOOD_GROUPS)
    height = models.CharField(max_length = 5)
    weight = models.CharField(max_length = 5)
    medical_allergies = models.CharField(max_length = 500)
    medications = models.CharField(max_length = 500)


