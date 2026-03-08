from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import singup, signin, listCreate, ListSend, delete

urlpatterns = [
    path('singup/', singup.as_view()),
    path('signin/', signin.as_view()),
    path('textbox/', listCreate.as_view()),
    path('list/', ListSend.as_view()),
    path('delete/<int:id>/', delete.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
]
