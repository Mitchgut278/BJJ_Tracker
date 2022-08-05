# Generated by Django 4.0.6 on 2022-08-04 19:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bjjtracker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MOTD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('completed', models.BooleanField(default=False)),
                ('technique', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bjjtracker.technique')),
            ],
        ),
    ]