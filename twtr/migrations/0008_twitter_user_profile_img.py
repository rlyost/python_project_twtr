# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-30 00:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twtr', '0007_auto_20180330_0017'),
    ]

    operations = [
        migrations.AddField(
            model_name='twitter_user',
            name='profile_img',
            field=models.CharField(max_length=255, null=True),
        ),
    ]