# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-25 21:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pagrindinis', '0025_remove_siuntiniai_vezejas'),
    ]

    operations = [
        migrations.AddField(
            model_name='siuntiniai',
            name='vezejas',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_vezejas', to=settings.AUTH_USER_MODEL),
        ),
    ]
