# Generated by Django 2.2.24 on 2021-07-20 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consignment', '0020_auto_20210720_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderconsignment',
            name='info_internal_shipment_number',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='orderconsignment',
            name='info_proxy',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name=''),
        ),
    ]
