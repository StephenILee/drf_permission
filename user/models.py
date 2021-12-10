from django.db import models as m
from django.contrib.auth.models import User


class Info(m.Model):
    user = m.OneToOneField(User, on_delete=m.CASCADE)
    name = m.CharField(max_length=100)
    mobile = m.CharField(max_length=100)


class Group(m.Model):
    user = m.ManyToManyField(User, blank=True)
    name = m.CharField(max_length=100)
