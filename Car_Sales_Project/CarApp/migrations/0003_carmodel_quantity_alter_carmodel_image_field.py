# Generated by Django 5.0 on 2024-01-14 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CarApp', '0002_alter_carmodel_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='carmodel',
            name='quantity',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='carmodel',
            name='image_field',
            field=models.ImageField(blank=True, null=True, upload_to='CarApp/media/images/'),
        ),
    ]