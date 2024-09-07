from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.utils import timezone
from elearning.models import UserExpiry

class SubscriptionCheckMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.user.is_authenticated:
            try:
                user_expiry = UserExpiry.objects.get(user=request.user)
                if not user_expiry.is_subscription_active():
                    return redirect(reverse('subscription_expired'))
            except UserExpiry.DoesNotExist:
                # Handle the case where UserExpiry does not exist for the user
                return redirect(reverse('subscription_expired'))
        return None
