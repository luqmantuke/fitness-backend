from django.db import models
from django.contrib.auth.models import AbstractUser, User
from ommyfitness.settings import AUTH_USER_MODEL
from django.conf import settings


class OTP(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    otp_value = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=20, blank=True, null=True)
