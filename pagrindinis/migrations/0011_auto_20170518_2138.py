# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-18 18:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagrindinis', '0010_auto_20170518_2058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='miestai',
            name='salis_miestas',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
