# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-18 17:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagrindinis', '0008_auto_20170518_2046'),
    ]

    operations = [
        migrations.AddField(
            model_name='miestai',
            name='salis_miestas',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]