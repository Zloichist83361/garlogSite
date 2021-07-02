# Generated by Django 2.2.2 on 2021-06-30 06:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consignment', '0007_auto_20210630_0915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderconsignment',
            name='document_height',
            field=models.DecimalField(blank=True, decimal_places=2, default='3', max_digits=5, null=True, validators=[django.core.validators.MaxValueValidator(4)], verbose_name='Высота(см)*'),
        ),
        migrations.AlterField(
            model_name='orderconsignment',
            name='document_length',
            field=models.DecimalField(blank=True, decimal_places=2, default='31', max_digits=5, null=True, validators=[django.core.validators.MaxValueValidator(31)], verbose_name='Длина(см)*'),
        ),
        migrations.AlterField(
            model_name='orderconsignment',
            name='document_weight',
            field=models.DecimalField(blank=True, decimal_places=2, default='2', max_digits=5, null=True, validators=[django.core.validators.MaxValueValidator(2)], verbose_name='Вес(кг)*'),
        ),
        migrations.AlterField(
            model_name='orderconsignment',
            name='document_width',
            field=models.DecimalField(blank=True, decimal_places=2, default='25', max_digits=5, null=True, validators=[django.core.validators.MaxValueValidator(25)], verbose_name='Ширина(см)*'),
        ),
        migrations.AlterField(
            model_name='orderconsignment',
            name='height_one',
            field=models.DecimalField(blank=True, decimal_places=2, default='0,1', max_digits=5, null=True, verbose_name='Высота(м)*'),
        ),
        migrations.AlterField(
            model_name='orderconsignment',
            name='length_one',
            field=models.DecimalField(blank=True, decimal_places=2, default='0,1', max_digits=5, null=True, verbose_name='Длина(м)*'),
        ),
        migrations.AlterField(
            model_name='orderconsignment',
            name='place_quantity',
            field=models.DecimalField(blank=True, decimal_places=2, default='1', max_digits=5, null=True, verbose_name='Количество*'),
        ),
        migrations.AlterField(
            model_name='orderconsignment',
            name='volume_one',
            field=models.DecimalField(blank=True, decimal_places=2, default='0,1', max_digits=5, null=True, verbose_name='Объем(м3)*'),
        ),
        migrations.AlterField(
            model_name='orderconsignment',
            name='weight_one',
            field=models.DecimalField(blank=True, decimal_places=2, default='1', max_digits=5, null=True, verbose_name='Вес(кг)*'),
        ),
        migrations.AlterField(
            model_name='orderconsignment',
            name='width_one',
            field=models.DecimalField(blank=True, decimal_places=2, default='0,1', max_digits=5, null=True, verbose_name='Ширина(м)*'),
        ),
    ]