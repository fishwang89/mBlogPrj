# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-29 08:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='update_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
