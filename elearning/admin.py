from django.contrib import admin
from elearning.models import Year, Subject, Unit, Lesson, UserExpiry
from django.contrib.sessions.models import Session

# Register your models here.
admin.site.register((Year, Subject, Unit, Lesson, Session, UserExpiry))
