# Generated by Django 4.1.1 on 2023-05-14 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videos',
            name='video_url',
            field=models.CharField(max_length=1000),
        ),
    ]
