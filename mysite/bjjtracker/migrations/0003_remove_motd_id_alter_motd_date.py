# Generated by Django 4.0.6 on 2022-08-05 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bjjtracker', '0002_motd'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='motd',
            name='id',
        ),
        migrations.AlterField(
            model_name='motd',
            name='date',
            field=models.DateField(auto_now=True, primary_key=True, serialize=False),
        ),
    ]