# Generated by Django 3.0.8 on 2020-07-24 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
        ('perfiles', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PerfilesPluginModel',
        ),
    ]
