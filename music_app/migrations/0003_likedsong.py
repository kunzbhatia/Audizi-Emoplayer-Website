# Generated by Django 2.2.5 on 2021-01-18 13:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('music_app', '0002_history'),
    ]

    operations = [
        migrations.CreateModel(
            name='LikedSong',
            fields=[
                ('liked_id', models.AutoField(primary_key=True, serialize=False)),
                ('music_id', models.CharField(default='', max_length=10000000)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
