# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-26 09:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagrindinis', '0026_siuntiniai_vezejas'),
    ]

    operations = [
        migrations.AddField(
            model_name='siuntiniai',
            name='siuntinio_stadija',
            field=models.IntegerField(default=0),
        ),
    ]
