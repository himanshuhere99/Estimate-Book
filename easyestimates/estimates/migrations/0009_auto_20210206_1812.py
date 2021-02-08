# Generated by Django 3.1.2 on 2021-02-06 18:12

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estimates', '0008_unit_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='item_mrp',
        ),
        migrations.RemoveField(
            model_name='item',
            name='item_rate',
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_mrp', models.IntegerField(blank=True, null=True)),
                ('item_rate', models.IntegerField(blank=True, null=True)),
                ('pub_date', models.DateTimeField(default=datetime.datetime.now, verbose_name='date published')),
                ('unit', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='estimates.unit')),
            ],
        ),
    ]