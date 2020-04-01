from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms.widgets import SelectDateWidget
from django.contrib.auth.models import  User
from django.contrib.auth import get_user_model
from django.conf import settings
from django import forms
from django.core.validators import MaxValueValidator

# Create your models here.

class Phone(AbstractUser):
    phone_number = models.CharField(('phone number'),
        help_text=('Field to save the phone number of the user.'), max_length=15, null=False,blank=False,error_messages={
               'required': 'Please enter your Phone Number'
                })
    username=models.CharField(max_length=20,default='user',unique=True)
    date_authorized=models.DateTimeField(auto_now_add=True)
    status=models.CharField(default='INACTIVE', max_length=10)

    def __str__(self):
        return self.username
    

class OneTimePassword(models.Model):
    phone=models.ForeignKey(Phone,on_delete=models.PROTECT,null=True,blank=True)
    pin=models.CharField(max_length=6)
    date_created=models.DateTimeField(auto_now_add=True)
    expiry_date=models.DateTimeField()
    used=models.BooleanField(null=True)

    def __str__(self):
        return self.pin