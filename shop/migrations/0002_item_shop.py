# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-04-01 10:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='shop',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='shop.Shop'),
            preserve_default=False,
        ),
    ]
