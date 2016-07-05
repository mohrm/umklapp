# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-05 14:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('umklapp', '0022_remove_story_skipvote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='started_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stories_created', to=settings.AUTH_USER_MODEL),
        ),
    ]