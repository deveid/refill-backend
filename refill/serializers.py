from rest_framework import serializers
from .models import Phone,OneTimePassword

class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model=Phone
        fields=("id","phone_number","username",)
        exclude_fields = '__all__'

class OTPSerializer(serializers.ModelSerializer):
    class Meta:
        model=OneTimePassword
        fields=("pin","date_created","phone","expiry_date")
        exclude_fields='__all__'
        depth=1