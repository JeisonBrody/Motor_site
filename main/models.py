from django.db import models


class Car(models.Model):
    brand_car = models.CharField(max_length=50, verbose_name="Марка авто")
    brand_image = models.ImageField(upload_to='photos/car', verbose_name="Изображение авто", blank=True, default="photos/car/error_img.jpg")

    def __str__(self):
        return self.brand_car

    class Meta:
        verbose_name = 'Марка Авто'  # Название в Main
        verbose_name_plural = 'Марки авто'


class Engine(models.Model):
    engine = models.CharField(max_length=50, verbose_name="Двигатель")

    def __str__(self):
        return self.engine

    class Meta:
        verbose_name = 'Двигатель'  # Название в Main
        verbose_name_plural = 'Двигатели'
