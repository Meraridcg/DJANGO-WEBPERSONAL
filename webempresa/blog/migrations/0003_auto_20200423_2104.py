# Generated by Django 3.0.5 on 2020-04-24 02:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200422_2337'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created'], 'verbose_name': 'Entrada', 'verbose_name_plural': 'Entradas'},
        ),
    ]
