# Generated by Django 3.1.2 on 2021-02-06 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estimates', '0010_auto_20210206_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unit',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estimates.item'),
        ),
    ]
