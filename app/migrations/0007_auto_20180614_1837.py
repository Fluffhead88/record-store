# Generated by Django 2.0.6 on 2018-06-14 18:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_remove_album_band'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='band',
            name='user',
        ),
        migrations.AddField(
            model_name='album',
            name='band',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='app.Band'),
        ),
        migrations.AddField(
            model_name='band',
            name='author',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
