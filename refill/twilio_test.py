from twilio.rest import Client


TWILIO_ACCOUNT_SID='ACdf698e09be21a25593f78c94974882cf'
TWILIO_AUTH_TOKEN='737054aff4d9989d50a792d0f0b8cbe3'
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

message = client.messages \
                .create(
                     body="Your otp is 1212",
                     from_='+12064586641',
                     to='+2348079895427'
                 )

print(message.sid)