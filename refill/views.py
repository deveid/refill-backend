from django.shortcuts import render
from django_twilio.decorators import twilio_view
from twilio.twiml.messaging_response import MessagingResponse
from .models import Phone
from .models import OneTimePassword
from .serializers import PhoneSerializer, OTPSerializer
from rest_framework import viewsets
from twilio.rest import Client
from .generate_otp import hotp
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status,generics
from rest_framework.views import APIView
from datetime import tzinfo, timedelta, datetime
from django.utils import timezone
from rest_framework import generics


TWILIO_ACCOUNT_SID='ACdf698e09be21a25593f78c94974882cf'
TWILIO_AUTH_TOKEN='737054aff4d9989d50a792d0f0b8cbe3'
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
twilio_phone="+12064586641"

class PhoneView(APIView):
    queryset=Phone.objects.all()
    serializer_class=PhoneSerializer
    
    
    def post(self,request):
        serializer = PhoneSerializer(data=request.data)
        if serializer.is_valid():
            digits=serializer.validated_data.get('phone_number')
            user_name=serializer.validated_data.get('username')
            otp=hotp()
            message = client.messages \
                    .create(
                         body="Your Verfication Code for Refill is "+otp+".This code expires in 10 minutes.Do not share with anyone.",
                         from_=twilio_phone,
                        to=digits
                        )

            expire_date=datetime.now(tz=timezone.utc)+timedelta(minutes=10)
            serializer.save()

            #saving otp to OTP models from phone model's
            present_id=Phone.objects.get(username=user_name)            
            OneTimePassword.objects.create(phone=present_id,pin=otp,
                                            expiry_date=expire_date)
            
            data={
                    'phone_number':digits,
                    'pin':otp,
                    "expire_date":expire_date,
                    "date_created":datetime.now(tz=timezone.utc)
                    }

            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OTPView(generics.ListAPIView):
    queryset=OneTimePassword.objects.all()
    serializer_class=OTPSerializer


