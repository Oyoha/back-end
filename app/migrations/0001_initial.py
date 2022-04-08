# Generated by Django 4.0.3 on 2022-04-07 15:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, validators=[django.core.validators.MinLengthValidator(3)])),
                ('weight', models.FloatField(validators=[django.core.validators.MinValueValidator(1.0), django.core.validators.MaxValueValidator(500.0)])),
                ('color', models.CharField(choices=[('R', 'Красный'), ('G', 'Зеленый'), ('B', 'Синий')], default='R', max_length=1)),
            ],
        ),
    ]
