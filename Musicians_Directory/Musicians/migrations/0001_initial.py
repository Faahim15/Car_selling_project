# Generated by Django 5.0 on 2024-01-13 08:42

import Musicians.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MusicianModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=100)),
                ('Last_name', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=254)),
                ('Phone_number', models.CharField(max_length=11, validators=[Musicians.models.validate_phone_number_length])),
                ('Instrument_type', models.CharField(max_length=50)),
            ],
        ),
    ]