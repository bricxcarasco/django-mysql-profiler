# Generated by Django 3.2.4 on 2021-06-24 12:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=200, verbose_name='Last Name')),
                ('email', models.CharField(max_length=200, unique=True, verbose_name='Email')),
                ('position', models.CharField(max_length=200, verbose_name='Position')),
                ('created_at', models.DateTimeField(default=datetime.datetime(2021, 6, 24, 12, 28, 8, 222527, tzinfo=utc))),
            ],
        ),
    ]