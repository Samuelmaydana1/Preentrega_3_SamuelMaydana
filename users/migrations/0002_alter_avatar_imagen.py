# Generated by Django 5.0.7 on 2024-08-05 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avatar',
            name='imagen',
            field=models.ImageField(default='avatares/avatar-default.png', upload_to='avatares'),
        ),
    ]
