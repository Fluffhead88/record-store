# Generated by Django 2.0.6 on 2018-06-14 18:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_remove_album_band'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='user',
        ),
    ]
