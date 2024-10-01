from django.urls import path
from .views import register, success, main


urlpatterns = [
    path('register/',register,name='register'),
    path('success/',success, name='success'),
    path('main/',main,name='main')
]
