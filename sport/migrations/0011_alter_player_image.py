# Generated by Django 4.2.6 on 2023-12-09 18:29

from django.db import migrations, models
import sport.models


class Migration(migrations.Migration):

    dependencies = [
        ('sport', '0010_alter_player_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='image',
            field=models.ImageField(upload_to=sport.models.player_upload_to_name),
        ),
    ]
