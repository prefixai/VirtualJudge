# Generated by Django 2.1.2 on 2018-12-05 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=20, unique=True)),
                ('email', models.EmailField(max_length=256, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('accepted', models.IntegerField(default=0)),
                ('submitted', models.IntegerField(default=0)),
                ('hook', models.URLField(blank=True, null=True)),
                ('nickname', models.CharField(max_length=20, null=True)),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]