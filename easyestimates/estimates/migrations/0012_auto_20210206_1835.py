# Generated by Django 3.1.2 on 2021-02-06 18:35

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estimates', '0011_auto_20210206_1813'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estimates',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='estimates',
            name='item_mrp',
        ),
        migrations.RemoveField(
            model_name='estimates',
            name='item_name',
        ),
        migrations.RemoveField(
            model_name='estimates',
            name='item_rate',
        ),
        migrations.RemoveField(
            model_name='estimates',
            name='pub_date',
        ),
        migrations.RemoveField(
            model_name='estimates',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='estimates',
            name='unit',
        ),
        migrations.AddField(
            model_name='estimates',
            name='estimate_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='customer',
            name='customer_mobile_number',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_code',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_name',
            field=models.CharField(max_length=100),
        ),
        migrations.CreateModel(
            name='Estimate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=50)),
                ('item_mrp', models.IntegerField(blank=True, null=True)),
                ('item_rate', models.IntegerField(blank=True, null=True)),
                ('unit', models.CharField(max_length=20)),
                ('quantity', models.IntegerField(default=0)),
                ('amount', models.IntegerField(default=0)),
                ('pub_date', models.DateTimeField(default=datetime.datetime.now, verbose_name='date published')),
                ('estimate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estimates.estimates')),
            ],
        ),
    ]
