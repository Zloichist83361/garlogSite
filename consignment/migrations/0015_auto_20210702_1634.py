# Generated by Django 2.2.24 on 2021-07-02 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consignment', '0014_auto_20210702_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderconsignment',
            name='passport_individual',
            field=models.IntegerField(blank=True, null=True, verbose_name='Серия и номер выбранного документа*'),
        ),
    ]
