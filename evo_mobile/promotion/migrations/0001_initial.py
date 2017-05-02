# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-22 04:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('expired', models.DateField(verbose_name='expired date')),
                ('description', models.TextField(verbose_name='description')),
                ('terms', models.TextField(verbose_name='terms & conditions')),
                ('thumbnail', models.ImageField(upload_to='images/promotions/%Y/%m')),
            ],
        ),
    ]
