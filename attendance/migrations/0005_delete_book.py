# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-06 15:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0004_book_pages'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Book',
        ),
    ]
