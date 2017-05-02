from django.db import models
from django.contrib.auth.models import User

from event.models import Ticket, Event

# class Payment(models.Model):
#     ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
#     event = models.ForeignKey(Event, on_delete=models.CASCADE)
#     price = models.FloatField()
#     date = models.DateTimeField(auto_now_add=True)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)

# class Recipe(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4)
#     event = models.ForeignKey(Event, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     price = models.FloatField()