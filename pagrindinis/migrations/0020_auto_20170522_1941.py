# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-22 18:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagrindinis', '0019_vezejas_telefono_numeris'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siuntiniai',
            name='siuntinio_aukstis',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='siuntiniai',
            name='siuntinio_ilgis',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='siuntiniai',
            name='siuntinio_plotis',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='siuntiniai',
            name='siuntinio_svoris',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='siuntiniai',
            name='sukurimo_data',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
