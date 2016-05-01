from __future__ import unicode_literals
from django.db import models

from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    pass


class Relationship(models.Model):
    pass


class Project(models.Model):
    pass
