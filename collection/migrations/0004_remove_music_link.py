# Generated by Django 4.1.1 on 2022-12-06 07:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0003_music_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='music',
            name='link',
        ),
    ]
