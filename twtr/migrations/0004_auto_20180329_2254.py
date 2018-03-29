# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-29 22:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twtr', '0003_twitter_user_user_since'),
    ]

    operations = [
        migrations.AlterField(
            model_name='twitter_user',
            name='time_zone',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='twitter_user',
            name='user_since',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]