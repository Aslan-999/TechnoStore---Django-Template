# Generated by Django 4.1.3 on 2022-11-24 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sliderimage',
            name='image',
            field=models.ImageField(upload_to='slider-images/'),
        ),
    ]