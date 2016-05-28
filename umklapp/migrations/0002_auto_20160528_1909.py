# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-28 19:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('umklapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teller',
            name='corresponding_story',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='corresponding_story', to='umklapp.Story'),
        ),
    ]