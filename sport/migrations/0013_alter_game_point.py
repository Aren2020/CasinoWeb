# Generated by Django 4.2.6 on 2023-12-09 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sport', '0012_team_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='point',
            field=models.IntegerField(blank=True),
        ),
    ]
