# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-26 14:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tadmin', '0005_comment_best_commnet'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='tag',
        ),
    ]