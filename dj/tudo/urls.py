from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import singup, signin

urlpatterns = [
    path('singup/', singup.as_view()),
    path('signin/', signin.as_view()),
]
