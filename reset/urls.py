# urls.py
from django.urls import path
from .views import reset_password

urlpatterns = [
    # Other URL patterns...
    path('reset_password/', reset_password, name='reset_password'),
]
