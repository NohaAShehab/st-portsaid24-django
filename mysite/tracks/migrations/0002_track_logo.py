# Generated by Django 5.0.7 on 2024-07-31 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='tracks/logos'),
        ),
    ]
