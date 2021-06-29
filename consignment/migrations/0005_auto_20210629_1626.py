# Generated by Django 2.2.2 on 2021-06-29 13:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consignment', '0004_auto_20210629_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderconsignment',
            name='weight_one',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0.01)], verbose_name='Вес(кг)'),
        ),
    ]