# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-19 19:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fit', '0010_dish_diet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='description',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='dish',
            name='image',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='category',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='description',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='lat',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='lng',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
