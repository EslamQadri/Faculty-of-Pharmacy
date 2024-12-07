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

from django.urls import resolve
from elearning.models import Lecture
class SubscriptionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        
        if request.user.is_authenticated:
            if not request.user.is_superuser:
            # Resolve the current view name
                resolver_match = resolve(request.path)
                view_name = resolver_match.view_name
 
                # Check if the view name matches lecture or lecture_view
                if view_name in ["lecture", "lecture_view"]:
                    try:
                        # Check if the user has a subscription
                        user_expiry = UserExpiry.objects.get(user=request.user)
                        if not user_expiry.is_subscription_active():
                            logout(request)
                            return redirect("subscription_expired")

                        # Check if the user is allowed to access the course
                        lecture_pk = resolver_match.kwargs.get("pk")
                        lecture = Lecture.objects.get(pk=lecture_pk)
                        if lecture.course not in user_expiry.courses.all():
                            return redirect("subscription_expired")

                    except (UserExpiry.DoesNotExist, Lecture.DoesNotExist):
                        logout(request)
                        return redirect("subscription_expired")
            return self.get_response(request)

        # Proceed with the request
        return self.get_response(request)
