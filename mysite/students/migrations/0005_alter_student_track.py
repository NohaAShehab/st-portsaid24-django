# Generated by Django 5.0.7 on 2024-07-30 08:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_student_created_at_student_updated_at_and_more'),
        ('tracks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='track',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tracks.track'),
        ),
    ]
