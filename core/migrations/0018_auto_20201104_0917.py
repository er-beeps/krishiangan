# Generated by Django 3.1.2 on 2020-11-04 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_auto_20201104_0749'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='image',
            field=models.ImageField(default='null', upload_to=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
