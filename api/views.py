# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from conversion.models import Currency
from .serializers import CurrencySerializer
import requests
import logging

# Configure logging
logging.basicConfig(filename='currency_conversion.log', level=logging.DEBUG)

@api_view(['GET', 'POST'])
def currency_data_api(request):
    if request.method == 'POST':
        serializer = CurrencySerializer(data=request.data)
        
        if serializer.is_valid():
            from_currency = serializer.validated_data.get("from_currency")
            to_currency = serializer.validated_data.get("to_currency")
            amount = serializer.validated_data.get("amount")

            if from_currency and to_currency and amount:
                try:
                    amount = float(amount)
                except ValueError:
                    logging.error("Invalid amount value")
                    return Response({"error": "Invalid amount value"}, status=status.HTTP_400_BAD_REQUEST)

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
                        serializer.save()  # Save the data to the database
                        return Response({"converted_amount": converted_amount}, status=status.HTTP_201_CREATED)
                    else:
                        logging.warning(f"Conversion rate for {to_currency} not found.")
                        return Response({"error": f"Conversion rate for {to_currency} not found."}, status=status.HTTP_400_BAD_REQUEST)
                else:
                    logging.error("Failed to retrieve data. Status code: %d", response.status_code)
                    return Response({"error": "Failed to retrieve currency data"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            else:
                logging.error("Invalid input provided.")
                return Response({"error": "Invalid input provided"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'GET':
        currencies = Currency.objects.all()
        serializer = CurrencySerializer(currencies, many=True)
        return Response(serializer.data)
