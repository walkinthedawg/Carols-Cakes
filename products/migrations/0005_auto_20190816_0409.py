# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-08-16 04:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_cakeuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='cakeuser',
            name='address',
            field=models.CharField(default=django.utils.timezone.now, max_length=250, verbose_name='Address line 1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cakeuser',
            name='city',
            field=models.CharField(default=django.utils.timezone.now, max_length=205, verbose_name='City'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cakeuser',
            name='state',
            field=models.CharField(default=django.utils.timezone.now, max_length=205, verbose_name='State'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cakeuser',
            name='zipcode',
            field=models.CharField(default=django.utils.timezone.now, max_length=90, verbose_name='Zip Code'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cakeuser',
            name='firstname',
            field=models.CharField(max_length=250, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='cakeuser',
            name='lastname',
            field=models.CharField(max_length=250, verbose_name='Last Name'),
        ),
    ]
