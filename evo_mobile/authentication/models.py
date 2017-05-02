from django.db import models
from django.contrib.auth.models import User


class UserDetail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    identifier = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    provience = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=50)

    class Meta():
        verbose_name = 'User Detail'

    def __str__(self):
        return self.first_name + self.last_name