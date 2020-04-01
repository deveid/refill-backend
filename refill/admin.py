from django.contrib import admin
from .models import Phone, OneTimePassword
# Register your models here.
admin.site.register(Phone)
admin.site.register(OneTimePassword)