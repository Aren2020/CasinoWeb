# Generated by Django 4.2.6 on 2023-12-09 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sport', '0007_alter_news_options_alter_news_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='position',
            field=models.CharField(default='replacement', max_length=10),
        ),
    ]
