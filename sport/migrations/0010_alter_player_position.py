# Generated by Django 4.2.6 on 2023-12-09 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sport', '0009_remove_team_image_alter_player_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='position',
            field=models.CharField(default='replacement', max_length=12),
        ),
    ]
