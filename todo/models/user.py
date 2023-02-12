from django.contrib.auth.models import User
from django.db import models
from avatar.models import Avatar
from todo.forms.register import RegisterForm


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.OneToOneField(Avatar, null=True, blank=True, on_delete=models.SET_NULL)
    # profile_picture = models.CharField(choices=RegisterForm.PROFILE_IMAGE_CHOICES, max_length=100)

