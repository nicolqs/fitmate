# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-19 18:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('fit', '0005_auto_20160319_1851'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=255)),
                ('lat', models.CharField(max_length=20)),
                ('lng', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=100)),
                ('zipcode', models.CharField(max_length=5)),
                ('category', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=50)),
                ('favourite_diet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fit.Diet')),
            ],
        ),
    ]
