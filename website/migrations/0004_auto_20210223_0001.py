# Generated by Django 3.1.6 on 2021-02-22 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_offers_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offers',
            name='price',
            field=models.IntegerField(max_length=200000),
        ),
    ]
