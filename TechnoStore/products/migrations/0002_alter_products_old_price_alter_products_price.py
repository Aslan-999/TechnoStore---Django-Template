# Generated by Django 4.1.3 on 2022-11-24 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='old_price',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.CharField(max_length=10),
        ),
    ]
