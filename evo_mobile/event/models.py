from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    thumbnail = models.ImageField(
        upload_to='images/categories', null=True, blank=True)

    class Meta():
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=255)
    thumbnail = models.ImageField(upload_to='images/events/%Y/%m')
    promotor = models.CharField(max_length=255, null=True, blank=True)
    start_date = models.DateField(verbose_name='start date', null=True)
    end_date = models.DateField(verbose_name='end date', null=True)
    start_time = models.TimeField(
        verbose_name='start time', null=True, blank=True)
    end_time = models.TimeField(verbose_name='end time', null=True, blank=True)
    terms = models.TextField(
        verbose_name='terms & conditions', null=True, blank=True)
    description = models.TextField(verbose_name='description')
    category = models.ForeignKey(Category, null=True, blank=True)

    def __str__(self):
        return self.name

    def minimum_price(self):
        price = self.tickets.aggregate(models.Min('price'))
        return price['price__min']

        
class Ticket(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='tickets')

    def __str__(self):
        return self.name


class Review(models.Model):
    name = models.CharField(max_length=255)
    rate = models.IntegerField()
    comment = models.TextField()
    event = models.IntegerField()