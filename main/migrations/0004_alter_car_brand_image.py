# Generated by Django 4.1.1 on 2022-09-29 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_car_brand_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='brand_image',
            field=models.ImageField(blank=True, height_field=100, upload_to='photos/car', verbose_name='Изображение авто', width_field=100),
        ),
    ]
