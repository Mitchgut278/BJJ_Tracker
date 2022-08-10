# Generated by Django 4.0.6 on 2022-08-09 23:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bjjtracker', '0009_technique_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='technique',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='MOTD',
        ),
    ]
