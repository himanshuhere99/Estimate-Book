# Generated by Django 3.1.2 on 2021-02-06 18:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estimates', '0015_auto_20210206_1852'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customers',
            name='pub_date',
        ),
        migrations.RemoveField(
            model_name='item',
            name='pub_date',
        ),
        migrations.RemoveField(
            model_name='rate',
            name='pub_date',
        ),
        migrations.RemoveField(
            model_name='unit',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='customers',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rate',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='unit',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime.now),
            preserve_default=False,
        ),
    ]
