# Generated by Django 4.2.6 on 2023-11-12 13:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sport', '0004_rename_sportsection_section_alter_section_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='members',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='game',
            name='point',
            field=models.IntegerField(default=100),
        ),
        migrations.AddField(
            model_name='game',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 8, 12, 56)),
        ),
        migrations.AddField(
            model_name='game',
            name='tv',
            field=models.BooleanField(default=False),
        ),
    ]