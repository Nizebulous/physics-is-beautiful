# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-10 20:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PiB', '0005_auto_20170110_2014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drawvector',
            name='xComponent',
            field=models.SmallIntegerField(blank=True, null=True, verbose_name=b'x-Component'),
        ),
        migrations.AlterField(
            model_name='drawvector',
            name='yComponent',
            field=models.SmallIntegerField(blank=True, null=True, verbose_name=b'y-Component'),
        ),
    ]