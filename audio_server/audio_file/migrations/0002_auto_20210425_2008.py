# Generated by Django 3.2 on 2021-04-25 20:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audio_file', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audiobook',
            name='upload_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 25, 20, 8, 21, 59906)),
        ),
        migrations.AlterField(
            model_name='podcast',
            name='upload_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 25, 20, 8, 21, 57905)),
        ),
        migrations.AlterField(
            model_name='song',
            name='upload_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 25, 20, 8, 21, 55910)),
        ),
    ]
