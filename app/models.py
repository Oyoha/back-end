from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator


class Products(models.Model):
    red = 'R'
    green = 'G'
    blue = 'B'
    COLOR = [(red, 'Красный'), (green, 'Зеленый'), (blue, 'Синий')]
    name = models.CharField(max_length=120, validators=[MinLengthValidator(3)])
    weight = models.FloatField(validators=[MinValueValidator(1.0), MaxValueValidator(500.0)])
    color = models.CharField(max_length=1, choices=COLOR, default=red)

    def get_absolute_url(self):
        return f'/'

