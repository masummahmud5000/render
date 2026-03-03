from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import singup

urlpatterns = [
    path('singup/', singup.as_view()),
]
