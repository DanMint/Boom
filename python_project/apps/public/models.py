from django.contrib.auth.models import User
from django.db import models

# to conect ppl by there intersts
from django.urls import reverse


class Products(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()

