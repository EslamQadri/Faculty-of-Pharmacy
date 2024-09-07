from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


# Create your models here.
class Year(models.Model):
    name = models.CharField(_("Year"), max_length=255)

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        verbose_name = "السنة_الدراسية"
        verbose_name_plural = "السنه_الدراسية"


class Subject(models.Model):
    name = models.CharField(_("Subject"), max_length=255)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        verbose_name = "المادة"
        verbose_name_plural = "المادة"


class Unit(models.Model):
    Subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    name = models.CharField(_("Unit"), max_length=255)

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        verbose_name = "الباب"
        verbose_name_plural = "الباب"


class Lesson(models.Model):
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    title = models.CharField(_("video name"), max_length=255)
    video = models.FileField(upload_to="videos/")
    description = models.TextField(
        "وصف الفيديو ", max_length=2550, null=True, blank=True
    )
    number = models.PositiveIntegerField("رقم الدرس ")

    class Meta:
        verbose_name = "الدرس"
        verbose_name_plural = "الدرس"

    def __str__(self) -> str:
        return f"{self.title}"

from django.utils import timezone
class UserExpiry(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    form = models.DateField("بداية الاشتراك")
    to = models.DateField("نهاية الاشتراك")
    def is_subscription_active(self):
        today = timezone.now().date()
        return self.form <= today <= self.to

    class Meta:
        verbose_name = "مدة الاشتراك"
        verbose_name_plural = "مدة الاشتراك"

    def __str__(self) -> str:
        return f"{self.user.get_full_name()}"


"""
to do
test in phone 
make supsctption system 
and update en ar 

"""
