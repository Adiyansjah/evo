# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-22 11:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promotion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promotion',
            name='terms',
            field=models.TextField(blank=True, null=True, verbose_name='terms & conditions'),
        ),
    ]
