# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-25 11:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagrindinis', '0022_auto_20170522_2003'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='siuntejas',
            name='pag_surinkimas_antradienis',
        ),
        migrations.RemoveField(
            model_name='siuntejas',
            name='pag_surinkimas_ketvirtadienis',
        ),
        migrations.RemoveField(
            model_name='siuntejas',
            name='pag_surinkimas_penktadienis',
        ),
        migrations.RemoveField(
            model_name='siuntejas',
            name='pag_surinkimas_pirmadienis',
        ),
        migrations.RemoveField(
            model_name='siuntejas',
            name='pag_surinkimas_sekmadienis',
        ),
        migrations.RemoveField(
            model_name='siuntejas',
            name='pag_surinkimas_sestadienis',
        ),
        migrations.RemoveField(
            model_name='siuntejas',
            name='pag_surinkimas_treciadienis',
        ),
        migrations.AddField(
            model_name='siuntejas',
            name='siuntejo_telefonas',
            field=models.CharField(default=5455245588, max_length=100),
            preserve_default=False,
        ),
    ]
