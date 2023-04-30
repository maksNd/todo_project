from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    list_display = ("first_name", "last_name")

    def __str__(self):
        return f"{self.username}, {self.email}, {self.first_name}, {self.last_name}"
