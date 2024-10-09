import datetime
from elearning.utilities import delete_all_unexpired_sessions_for_user

from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from elearning.models import Lesson, Year, Unit, Subject,UserExpiry


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


@login_required
def subject(request, pk):
    expiry=None
    if request.user.is_authenticated:
        try:
            expiry = UserExpiry.objects.get(user=request.user)
        except UserExpiry.DoesNotExist:
            expiry = None
    # y = Year.objects.get(pk=pk)
    subject_list = Subject.objects.filter(year_id=pk)
    # print(subject_list)
    return render(request, "subject.html", {"subject_list": subject_list,"expiry":expiry})


@login_required
def unit(request, pk):
    expiry=None
    if request.user.is_authenticated:
        try:
            expiry = UserExpiry.objects.get(user=request.user)
        except UserExpiry.DoesNotExist:
            expiry = None
    unit_list = Unit.objects.filter(Subject_id=pk)
    return render(request, "unit.html", {"unit_list": unit_list,"expiry":expiry})


@login_required
def lesson(request, pk):
    expiry=None
    if request.user.is_authenticated:
        try:
            expiry = UserExpiry.objects.get(user=request.user)
        except UserExpiry.DoesNotExist:
            expiry = None
    lesson_list = Lesson.objects.filter(unit_id=pk)
    # print(lesson_list)
    return render(request, "lesson.html", {"lesson_list": lesson_list,"expiry":expiry})


@login_required
def lesson_view(request, pk):
    expiry=None
    if request.user.is_authenticated:
        try:
            expiry = UserExpiry.objects.get(user=request.user)
        except UserExpiry.DoesNotExist:
            expiry = None
    lesson = Lesson.objects.get(pk=pk)
    # print(lesson)
    return render(request, "lesson_view.html", {"lesson": lesson,"expiry":expiry})
