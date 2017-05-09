from django.db import models
from django.contrib.auth.models import User

from event.models import Ticket, Event


class Payment(models.Model):
    code = models.CharField(max_length=255)
    method = models.CharField(max_length=255, null=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    price = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return self.code
