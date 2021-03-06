# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2018-10-31 07:19
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EvaDataDisplay',
            fields=[
                ('eva_id', models.CharField(default=uuid.uuid1, max_length=100, primary_key=True, serialize=False)),
                ('record_id', models.CharField(max_length=100)),
                ('user_id', models.CharField(max_length=100)),
                ('user_name', models.CharField(max_length=20)),
                ('server_id', models.CharField(max_length=100)),
                ('server_name', models.CharField(max_length=20)),
                ('eva_state', models.CharField(db_index=True, default='未评价', max_length=10)),
                ('star_num', models.CharField(db_index=True, max_length=1, null=True)),
                ('word_eva', models.TextField(max_length=500, null=True)),
                ('update_time', models.DateTimeField(auto_now=True, db_index=True, null=True)),
                ('created_time', models.DateTimeField(auto_now_add=True, db_index=True, null=True)),
            ],
            options={
                'db_table': 'evadatadisplay',
            },
        ),
    ]
