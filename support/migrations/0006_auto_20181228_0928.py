# Generated by Django 2.1.2 on 2018-12-28 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0005_support_oj_reuse'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='account',
            table='account',
        ),
        migrations.AlterModelTable(
            name='language',
            table='language',
        ),
    ]