# Generated by Django 4.2.4 on 2023-09-30 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_image_height_image_width'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='height',
            field=models.PositiveIntegerField(default=700),
        ),
        migrations.AlterField(
            model_name='image',
            name='width',
            field=models.PositiveIntegerField(default=400),
        ),
    ]
