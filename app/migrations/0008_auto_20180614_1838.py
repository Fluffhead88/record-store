# Generated by Django 2.0.6 on 2018-06-14 18:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20180614_1837'),
    ]

    operations = [
        migrations.RenameField(
            model_name='band',
            old_name='author',
            new_name='user',
        ),
    ]
