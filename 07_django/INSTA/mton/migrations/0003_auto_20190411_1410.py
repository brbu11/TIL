# Generated by Django 2.1.7 on 2019-04-11 05:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mton', '0002_client_hotel'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={'ordering': ('name',)},
        ),
    ]
