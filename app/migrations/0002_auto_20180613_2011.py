# Generated by Django 2.0.6 on 2018-06-13 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='release_date',
            field=models.CharField(default='No date provided', max_length=25),
        ),
        migrations.AlterField(
            model_name='band',
            name='date_formed',
            field=models.CharField(default='No date provided', max_length=25),
        ),
    ]