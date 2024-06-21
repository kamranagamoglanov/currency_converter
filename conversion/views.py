import logging
from django.shortcuts import render
from .models import Currency
import requests

# Configure logging
logging.basicConfig(filename='currency_conversion.log', level=logging.DEBUG)

def currency_data(request):
    converted_amount = None 

    if request.method == "GET":
        from_currency = request.GET.get("from_currency")
        to_currency = request.GET.get("to_currency")
        amount = request.GET.get("amount")

        if from_currency and to_currency and amount:
            try:
                amount = float(amount)
            except ValueError:
                logging.error("Invalid amount value")
                amount = None

            if amount is not None:
                link_currencies = "https://v6.exchangerate-api.com/v6/1cb86a7d10b1120477de4a54/latest/"
                full_link_currencies = link_currencies + from_currency
                response = requests.get(full_link_currencies)

                if response.status_code == 200:
                    data = response.json()
                    conversion_rates = data.get('conversion_rates', {})
                    to_currency_rate = conversion_rates.get(to_currency)

                    if to_currency_rate:
                        converted_amount = round(amount * to_currency_rate, 4)
                        logging.info(f"Converted amount: {converted_amount}")
                    else:
                        logging.warning(f"Conversion rate for {to_currency} not found.")
                else:
                    logging.error("Failed to retrieve data. Status code: %d", response.status_code)
            else:
                logging.error("Invalid amount provided.")

    data = Currency.objects.all()
    return render(request, "conversion/home.html", {"currency": data, "converted_amount": converted_amount})
