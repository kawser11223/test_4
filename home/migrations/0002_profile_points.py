# Generated by Django 5.1.3 on 2024-11-15 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='points',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
