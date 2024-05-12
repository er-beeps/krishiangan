# Generated by Django 3.2 on 2024-02-09 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0049_auto_20240208_1845'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='allow_password_change',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='verified_datetime',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
