from django.urls import include, path
from django.conf.urls import  url
from rest_framework import routers
from .views import PhoneView,OTPView

router = routers.DefaultRouter()
# router.register(r'get_otp', OTPView, basename='regis')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path(r'register', include(PhoneView.as_view(), namespace='regis')),
    url(r'^register/', PhoneView.as_view()),
    url(r'^otp/',OTPView.as_view()),
]