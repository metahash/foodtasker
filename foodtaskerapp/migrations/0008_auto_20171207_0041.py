# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-07 00:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodtaskerapp', '0007_auto_20171128_1112'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='driver',
            name='location',
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.DateTimeField(choices=[(1, 'Cooking'), (2, 'Ready'), (3, 'On the way'), (4, 'Delivered')]),
        ),
    ]