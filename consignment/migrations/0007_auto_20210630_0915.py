# Generated by Django 2.2.2 on 2021-06-30 06:15

import django.core.validators
from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('consignment', '0006_auto_20210629_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderconsignment',
            name='address_from',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Адрес*'),
        ),
        migrations.AlterField(
            model_name='orderconsignment',
            name='address_to',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Адрес*'),
        ),
        migrations.AlterField(
            model_name='orderconsignment',
            name='contact_person_entity',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Контактное лицо*'),
        ),
        migrations.AlterField(
            model_name='orderconsignment',
            name='declared_value',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Объявленная стоимость*'),
        ),
        migrations.AlterField(
            model_name='orderconsignment',
            name='document_height',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, validators=[django.core.validators.MaxValueValidator(4)], verbose_name='Высота(см)*'),
        ),
        migrations.AlterField(
            model_name='orderconsignment',
            name='document_length',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, validators=[django.core.validators.MaxValueValidator(31)], verbose_name='Длина(см)*'),
        ),
        migrations.AlterField(
            model_name='orderconsignment',
            name='document_weight',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, validators=[django.core.validators.MaxValueValidator(2)], verbose_name='Вес(кг)*'),
        ),
        migrations.AlterField(
            model_name='orderconsignment',
            name='document_width',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, validators=[django.core.validators.MaxValueValidator(25)], verbose_name='Ширина(см)*'),
        ),
        migrations.AlterField(
            model_name='orderconsignment',
            name='email_entity',
            field=models.EmailField(blank=True, max_length=255, null=True, verbose_name='Email*'),
        ),
        migrations.AlterField(
            model_name='orderconsignment',
            name='email_individual',
            field=models.EmailField(blank=True, max_length=255, null=True, verbose_name='Email*'),
        ),
        migrations.AlterField(
            model_name='orderconsignment',
            name='fio_entity',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Название компании*'),
        ),
        migrations.AlterField(
            model_name='orderconsignment',
            name='fio_individual',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='ФИО*'),
        ),
        migrations.AlterField(
            model_name='orderconsignment',
            name='height_one',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Высота(м)*'),
        ),
        migrations.AlterField(
            model_name='orderconsignment',
            name='inn_entity',
            field=models.IntegerField(blank=True, null=True, verbose_name='ИНН*'),
        ),
        migrations.AlterField(
            model_name='orderconsignment',
            name='length_one',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Длина(м)*'),
        ),
        migrations.AlterField(
            model_name='orderconsignment',
            name='passport_individual',
            field=models.IntegerField(blank=True, null=True, verbose_name='Серия и номер паспорта*'),
        ),
        migrations.AlterField(
            model_name='orderconsignment',
            name='phone_entity',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, unique=True, verbose_name='Контактный телефон*'),
        ),
        migrations.AlterField(
            model_name='orderconsignment',
            name='phone_individual',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, unique=True, verbose_name='Контактный телефон*'),
        ),
        migrations.AlterField(
            model_name='orderconsignment',
            name='place_quantity',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Количество*'),
        ),
        migrations.AlterField(
            model_name='orderconsignment',
            name='some_hardest',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Самое тяжелое(кг)*'),
        ),
        migrations.AlterField(
            model_name='orderconsignment',
            name='some_highest',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Самое высокое(м)*'),
        ),
        migrations.AlterField(
            model_name='orderconsignment',
            name='some_longest',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Самое длинное(м)*'),
        ),
        migrations.AlterField(
            model_name='orderconsignment',
            name='some_place_quantity',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Кол-во мест*'),
        ),
        migrations.AlterField(
            model_name='orderconsignment',
            name='some_volume',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Общий объем(м3)*'),
        ),
        migrations.AlterField(
            model_name='orderconsignment',
            name='some_weight',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Общий вес(кг)*'),
        ),
        migrations.AlterField(
            model_name='orderconsignment',
            name='some_widest',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Самое широкое(м)*'),
        ),
        migrations.AlterField(
            model_name='orderconsignment',
            name='terminal_from',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Терминал*'),
        ),
        migrations.AlterField(
            model_name='orderconsignment',
            name='terminal_to',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Терминал*'),
        ),
        migrations.AlterField(
            model_name='orderconsignment',
            name='third_person',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Город, имя, телефон*'),
        ),
        migrations.AlterField(
            model_name='orderconsignment',
            name='volume_one',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Объем(м3)*'),
        ),
        migrations.AlterField(
            model_name='orderconsignment',
            name='weight_one',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Вес(кг)*'),
        ),
        migrations.AlterField(
            model_name='orderconsignment',
            name='width_one',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Ширина(м)*'),
        ),
    ]
