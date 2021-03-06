# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-18 17:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pagrindinis', '0005_auto_20170517_1742'),
    ]

    operations = [
        migrations.CreateModel(
            name='Miestai',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('miesto_pavadinimas', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Salys',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salies_pavadinimas', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='siuntiniai',
            name='siuntinio_aukstis',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='miestai',
            name='salis',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pagrindinis.Salys'),
        ),
        migrations.AddField(
            model_name='siuntiniai',
            name='siuntinio_miestas',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='pagrindinis.Miestai'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='siuntiniai',
            name='siuntinio_salis',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='pagrindinis.Salys'),
            preserve_default=False,
        ),
    ]
