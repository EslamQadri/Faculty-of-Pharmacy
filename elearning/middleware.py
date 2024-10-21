from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.utils import timezone
from elearning.models import UserExpiry
from django.contrib.auth import  logout

class SubscriptionCheckMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path == reverse('subscription_expired'):
            return None
        if request.user.is_authenticated:
            if not request.user.is_superuser:
           
                try:
                    user_expiry = UserExpiry.objects.get(user=request.user)
                    
                    if not user_expiry.is_subscription_active():
                        logout(request)
                        return redirect('subscription_expired')
                except UserExpiry.DoesNotExist:
                    logout(request)
                    return redirect('subscription_expired')
            return None 
        return None
