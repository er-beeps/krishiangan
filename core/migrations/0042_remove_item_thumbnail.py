# Generated by Django 3.2.14 on 2023-01-23 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0041_biditem_is_withdrawn'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='thumbnail',
        ),
    ]
