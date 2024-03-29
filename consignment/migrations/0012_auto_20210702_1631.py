# Generated by Django 2.2.24 on 2021-07-02 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consignment', '0011_auto_20210702_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderconsignment',
            name='driver_license_individual',
            field=models.IntegerField(blank=True, null=True, verbose_name='Серия и номер водительского удостоверения*'),
        ),
        migrations.AlterField(
            model_name='orderconsignment',
            name='military_ID_individual',
            field=models.IntegerField(blank=True, null=True, verbose_name='Серия и номер военного билета*'),
        ),
    ]
