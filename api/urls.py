# urls.py
from django.urls import path
from .views import currency_data_api

urlpatterns = [
    path('', currency_data_api, name='currency_data_api'),
]
