# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-10 14:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=256)),
                ('downloadStatus', models.CharField(max_length=50)),
                ('processingStatus', models.CharField(max_length=50)),
                ('typeOfProcesses', models.TextField()),
                ('testResult', models.TextField()),
                ('created_at', models.DateTimeField(verbose_name='date published')),
                ('lastProcessed', models.DateTimeField(verbose_name='date')),
            ],
        ),
    ]
