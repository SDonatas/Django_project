# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-22 18:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pagrindinis', '0020_auto_20170522_1941'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='siuntiniai',
            name='siuntinio_miestas',
        ),
    ]
