# Generated by Django 2.0.6 on 2018-06-18 01:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20180615_1825'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='band',
        ),
        migrations.AddField(
            model_name='band',
            name='album',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='app.Album'),
            preserve_default=False,
        ),
    ]
