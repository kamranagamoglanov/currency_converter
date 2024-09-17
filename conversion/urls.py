from django.urls import path
from .views import currency_data


app_name = "conversion"

urlpatterns = [
    path("",
         currency_data,
         name="home")
]