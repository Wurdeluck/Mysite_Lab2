# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-07 06:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0008_auto_20160507_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='birth_year',
            field=models.PositiveIntegerField(null=True),
        ),
    ]