# Generated by Django 4.1.1 on 2022-12-06 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0002_music_date_created_music_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='music',
            name='link',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]