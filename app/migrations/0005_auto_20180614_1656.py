# Generated by Django 2.0.6 on 2018-06-14 16:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20180614_1642'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='band',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='app.Band'),
        ),
        migrations.AddField(
            model_name='album',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='band',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
