# Generated by Django 2.2.24 on 2021-07-22 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consignment', '0024_auto_20210722_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderconsignment',
            name='declared_value',
            field=models.DecimalField(blank=True, decimal_places=2, default='0', max_digits=5, null=True, verbose_name='Объявленная стоимость*'),
        ),
    ]
