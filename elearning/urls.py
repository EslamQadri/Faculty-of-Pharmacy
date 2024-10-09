from django.urls import path
from elearning.views import (
    home,
    years,
    subject,
    unit,
    lesson,
    lesson_view,
    login_view,
    logout_view,
    subscription_expired,
)

urlpatterns = [
    # path("", index),
    path("", home, name="home"),
    path("year", years, name="year"),
    path("year/<int:pk>", years, name="year_with_pk"),
    path("subjects/<int:pk>", subject, name="subjects"),
    path("units/<int:pk>", unit, name="units"),
    path("lessons/<int:pk>", lesson, name="lessons"),
    path("lesson_view/<int:pk>", lesson_view, name="lesson_view"),
    path("login", login_view, name="login"),
    path("logout", logout_view, name="logout"),
    path("subscription_expired",subscription_expired,name="subscription_expired"),
]
