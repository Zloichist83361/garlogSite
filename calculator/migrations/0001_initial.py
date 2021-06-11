# Generated by Django 2.2.2 on 2021-06-11 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calculate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cityto', models.CharField(max_length=255)),
                ('cityfrom', models.CharField(max_length=255)),
                ('weightto', models.CharField(default='', max_length=255)),
                ('weightfrom', models.CharField(default='', max_length=255)),
                ('inter_terminal', models.CharField(max_length=255)),
                ('pickup', models.CharField(max_length=255)),
                ('cargo_delivery', models.CharField(max_length=255)),
                ('premium', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Term',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cityto', models.CharField(max_length=255)),
                ('cityfrom', models.CharField(max_length=255)),
                ('term_standart_to', models.CharField(max_length=255)),
                ('term_standart_from', models.CharField(max_length=255)),
                ('term_express_to', models.CharField(max_length=255)),
                ('term_express_from', models.CharField(max_length=255)),
            ],
        ),
    ]
