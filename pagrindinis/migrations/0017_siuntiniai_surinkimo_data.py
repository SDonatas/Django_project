# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-21 12:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagrindinis', '0016_siuntiniai_pristatymo_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='siuntiniai',
            name='surinkimo_data',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
