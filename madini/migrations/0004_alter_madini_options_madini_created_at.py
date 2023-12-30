# Generated by Django 4.1.1 on 2023-05-16 15:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('madini', '0003_alter_madini_content'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='madini',
            options={'ordering': ['-created_at']},
        ),
        migrations.AddField(
            model_name='madini',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
