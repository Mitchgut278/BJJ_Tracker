# Generated by Django 3.1.6 on 2022-07-21 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bjjtracker', '0003_auto_20220721_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='technique',
            name='comments',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='technique',
            name='details',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='technique',
            name='steps',
            field=models.TextField(blank=True, null=True),
        ),
    ]