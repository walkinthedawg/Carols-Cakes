# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-08-11 05:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20190809_0304'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='cat_desc',
        ),
        migrations.RemoveField(
            model_name='product',
            name='cat_image',
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(default='', max_length=20),
        ),
    ]