# Generated by Django 4.0.6 on 2022-08-06 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bjjtracker', '0005_alter_technique_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='technique',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
