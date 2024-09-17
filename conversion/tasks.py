import requests
import datetime
import json

from random import randint

from django.shortcuts import render

from celery import shared_task


url = "https://v6.exchangerate-api.com/v6/1cb86a7d10b1120477de4a54/latest/azn"

@shared_task
def get_exchange_rates(_url):
    response = requests.get(_url)
    return response.json()

exchange_rates = get_exchange_rates(url)
print(exchange_rates)

def save_exchange_rates_to_file():
    exchange_rates = get_exchange_rates(url)
    filename = f"exchange_rates_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.json"
    
    with open(filename, 'w') as file:
        json.dump(exchange_rates, file, indent=4)
    
    print(f"Exchange rates saved to {filename}")

save_exchange_rates_to_file()
