# Generated by Django 4.2 on 2024-08-06 20:34

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0005_alter_avatar_imagen'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='avatar',
            unique_together={('user',)},
        ),
    ]
