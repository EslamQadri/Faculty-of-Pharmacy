from django.urls import path
from elearning.views import (
    home,
    years,
    course,
    # unit,
    lecture,
    lecture_view,
    login_view,
    logout_view,
    subscription_expired,
)

urlpatterns = [
    # path("", index),
    path("", home, name="home"),
    path("year", years, name="year"),
    path("year/<int:pk>", years, name="year_with_pk"),
    path("course/<int:pk>", course, name="course"),
    # path("units/<int:pk>", unit, name="units"),
    path("lecture/<int:pk>", lecture, name="lecture"),
    path("lecture_view/<int:pk>", lecture_view, name="lecture_view"),
    path("login", login_view, name="login"),
    path("logout", logout_view, name="logout"),
    path("subscription_expired",subscription_expired,name="subscription_expired"),
]
