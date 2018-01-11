# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-27 18:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodtaskerapp', '0005_orderdetail'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OrderDetail',
            new_name='OrderDetails',
        ),
        migrations.AlterField(
            model_name='order',
            name='driver',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='foodtaskerapp.Driver'),
        ),
    ]
