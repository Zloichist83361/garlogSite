# Generated by Django 2.2.24 on 2021-07-05 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consignment', '0016_auto_20210702_1636'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderconsignment',
            old_name='third_person',
            new_name='third_person_input_customer',
        ),
        migrations.AddField(
            model_name='orderconsignment',
            name='third_person_input_payer',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Город, имя, телефон*'),
        ),
    ]
