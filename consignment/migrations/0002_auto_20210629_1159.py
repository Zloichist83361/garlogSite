# Generated by Django 2.2.2 on 2021-06-29 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consignment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trackstatusconsignment',
            name='tracking_number_client',
            field=models.CharField(max_length=255, null=True, unique=True),
        ),
    ]
