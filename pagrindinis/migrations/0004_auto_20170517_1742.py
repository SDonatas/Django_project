# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-17 14:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagrindinis', '0003_auto_20170517_1737'),
    ]

    operations = [
        migrations.AddField(
            model_name='siuntiniai',
            name='siuntinio_ilgis',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='siuntiniai',
            name='siuntinio_plotis',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='siuntiniai',
            name='siuntinio_svoris',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]