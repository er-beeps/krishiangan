# Generated by Django 3.1.2 on 2020-11-08 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_auto_20201108_1015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='expiry_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='upload_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
