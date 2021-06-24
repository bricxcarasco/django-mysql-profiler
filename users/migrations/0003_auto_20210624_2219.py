# Generated by Django 3.2.4 on 2021-06-24 14:19

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210624_2144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 24, 14, 19, 2, 976356, tzinfo=utc)),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(default='null', max_length=254)),
                ('body', models.TextField(default='null')),
                ('status', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2021, 6, 24, 14, 19, 2, 976920, tzinfo=utc))),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='users.user')),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
    ]