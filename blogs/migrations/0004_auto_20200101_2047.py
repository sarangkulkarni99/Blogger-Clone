# Generated by Django 3.0.1 on 2020-01-01 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_post_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='post',
            name='status',
        ),
    ]
