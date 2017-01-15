from django.db import models


class MyUser(models.Model):
    uid = models.IntegerField(primary_key=True, unique=True)
    login = models.CharField(max_length=100)