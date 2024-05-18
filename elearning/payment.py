# views.py
import requests
from django.shortcuts import render, redirect
from django.conf import settings

def initiate_payment(request):
    # Get the necessary payment data from the request or your database
    amount = 100  # Example amount in cents (e.g., $1.00)
    order_id = 12345  # Example order ID
    currency = 'EGP'  # Example currency code

    # Prepare the request data for Paymob's API
    payload = {
            
        "delivery_needed": "false",
        "amount_cents": amount,
        "currency": currency,
        "order_id": order_id,
        "integration_id": settings.PAYMOB_INTEGRATION_ID,
        # Add more required parameters as needed
    }

    # Make a POST request to Paymob's API to initiate the payment
    response = requests.post(settings.PAYMOB_PAYMENT_URL, json=payload)
    payment_data = response.json()

    # Redirect the user to the payment page provided by Paymob
    payment_link = payment_data.get('payment_key', '')
    return redirect(payment_link)

def payment_callback(request):
    # Handle the payment callback from Paymob after the user completes the payment
    # Update your database with the payment status and other relevant information
    return render(request, 'payment/callback.html')
