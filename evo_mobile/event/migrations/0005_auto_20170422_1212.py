# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-22 05:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0004_auto_20170422_1211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='thumbnail',
            field=models.ImageField(null=True, upload_to='images/categories'),
        ),
    ]