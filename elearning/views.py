import datetime
from elearning.utilities import delete_all_unexpired_sessions_for_user

from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from elearning.models import Course, Year, UserExpiry,Lecture


# Create your views here.
# def index(request):
# return render(request, "base.html")


def login_view(request):
    if request.POST:
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:

            login(request, user)
            delete_all_unexpired_sessions_for_user(request.user, request.session)
            # print((request.session.encode()))

            # print(dir(request.session))

            return redirect("year")
        else:

            # Return an 'invalid login' error message.
            return redirect("login")

    return render(request, "login.html")

def subscription_expired(request):
    return render(request, "SubscriptionExpired.html")
    
@login_required
def logout_view(request):
    logout(request)
    return redirect("login")



def home(request):
    expiry=None
    if request.user.is_authenticated:
        try:
            expiry = UserExpiry.objects.get(user=request.user)
        except UserExpiry.DoesNotExist:
            expiry = None
    return render(request, "home.html",{"expiry":expiry})


@login_required
def years(request, pk=None):
    expiry=None
    if request.user.is_authenticated:
        try:
            expiry = UserExpiry.objects.get(user=request.user)
        except UserExpiry.DoesNotExist:
            expiry = None
    years_list = Year.objects.all()
    if pk:
        years_list = Year.objects.all(pk=pk)
    return render(request, "year.html", {"years_list": years_list,"expiry":expiry})

# we are change from Subject to Course in models
@login_required
def course(request, pk):
    expiry=None
    if request.user.is_authenticated:
        try:
            expiry = UserExpiry.objects.get(user=request.user)
            #print(expiry.courses.all())
        except UserExpiry.DoesNotExist:
            expiry = None
    # y = Year.objects.get(pk=pk)
    course_list = expiry.courses.all()
    # print(subject_list)
    return render(request, "course.html", {"course_list": course_list,"expiry":expiry})


# @login_required
# def unit(request, pk):
#     expiry=None
#     if request.user.is_authenticated:
#         try:
#             expiry = UserExpiry.objects.get(user=request.user)
#         except UserExpiry.DoesNotExist:
#             expiry = None
#     unit_list = Unit.objects.filter(Subject_id=pk)
#     return render(request, "unit.html", {"unit_list": unit_list,"expiry":expiry})

# we are change from lesson to Lecture
@login_required
def lecture(request, pk):
    expiry=None
    if request.user.is_authenticated:
        try:
            expiry = UserExpiry.objects.get(user=request.user)
            
            
        except UserExpiry.DoesNotExist:
            expiry = None
    lecture_list = Lecture.objects.filter(course_id=pk)
    # print(lesson_list)
    return render(request, "lecture.html", {"lecture_list": lecture_list,"expiry":expiry})


@login_required
def lecture_view(request, pk):
    expiry=None
    if request.user.is_authenticated:
        try:
            expiry = UserExpiry.objects.get(user=request.user)
        except UserExpiry.DoesNotExist:
            expiry = None
    lecture = Lecture.objects.get(pk=pk)
    # print(lesson)
    return render(request, "lecture_view.html", {"lecture": lecture,"expiry":expiry})
