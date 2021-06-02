from django.db import models


class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=50, default="")
    role = models.CharField(max_length=50, default="")
    ifLogged = models.BooleanField(default=False)
    accessToken = models.CharField(max_length=500, null=True, default="")


def __str__(self):
    return "{} -{}".format(self.email)
