from django.urls import path
from .views import register, homeView

urlpatterns = [
    path('register/', register, name='register'),
    path('', homeView, name='home'),
]