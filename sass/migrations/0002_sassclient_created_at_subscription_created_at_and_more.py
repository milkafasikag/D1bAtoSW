# Generated by Django 4.2.4 on 2024-01-01 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sass', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sassclient',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='subscription',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='subscriptionplan',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]