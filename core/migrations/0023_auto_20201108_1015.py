# Generated by Django 3.1.2 on 2020-11-08 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_auto_20201108_1014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='upload_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
