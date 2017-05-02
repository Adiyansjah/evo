from django.db import models


class Promotion(models.Model):
    name = models.CharField(max_length=255)
    expired = models.DateField(verbose_name='expired date')
    description = models.TextField(verbose_name='description')
    terms = models.TextField(verbose_name='terms & conditions', null=True, blank=True)
    thumbnail = models.ImageField(upload_to='images/promotions/%Y/%m')

    def __str__(self):
        return self.name