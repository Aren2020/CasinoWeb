# Generated by Django 4.2.6 on 2023-12-09 18:39

from django.db import migrations, models
import sport.models


class Migration(migrations.Migration):

    dependencies = [
        ('sport', '0011_alter_player_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='image',
            field=models.ImageField(blank=True, upload_to=sport.models.team_upload_to_name),
        ),
    ]
