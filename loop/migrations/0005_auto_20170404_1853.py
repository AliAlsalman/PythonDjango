# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-05 01:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loop', '0004_auto_20170227_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='company_logo',
            field=models.ImageField(null=True, upload_to='company_logo/', verbose_name='Company Logo '),
        ),
    ]