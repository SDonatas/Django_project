# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-20 21:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pagrindinis', '0014_siuntejas_siuntejas_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='miestai',
            name='salis_miestas',
            field=models.CharField(blank=True, max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='siuntiniai',
            name='vezejas',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pagrindinis.Vezejas'),
        ),
    ]
