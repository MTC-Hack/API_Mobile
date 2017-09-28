# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-28 10:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rat', '0006_auto_20170928_1007'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email')),
                ('phone', models.CharField(default='', max_length=11, verbose_name='phone')),
                ('firstname', models.CharField(default='', max_length=255, verbose_name='firstname')),
                ('lastname', models.CharField(default='', max_length=255, verbose_name='lastname')),
                ('is_staff', models.BooleanField(default=False, verbose_name='is_staff')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='is_staff')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]