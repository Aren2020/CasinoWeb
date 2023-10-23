# Generated by Django 4.2.6 on 2023-10-23 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sport', '0002_team_player_game'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='draw',
            field=models.DecimalField(decimal_places=2, default=1.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='game',
            name='lose',
            field=models.DecimalField(decimal_places=2, default=1.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='game',
            name='win',
            field=models.DecimalField(decimal_places=2, default=1.0, max_digits=10),
        ),
    ]
