from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    # password = models.CharField(max_length=50)
    joined_date = models.DateTimeField(auto_now_add=True)
    USER = 'user'
    CHEF = 'chef'
    ROLE_CHOISES = [
        (USER, 'User'),
        (CHEF, 'Chef')
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOISES)

UNIT_CHOICES = [
    ('g', 'gram'),
    ('kg', 'kilogram'),
    ('l', 'liter'),
    ('ml', 'milliliter'),
    ('pcs', 'piece'),
]


class Dish(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    preparation_method = models.TextField()
    image = models.URLField(max_length=200)
    chef = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField()
    updated_at = models.DateField(auto_now_add=True)

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.FloatField()
    unit = models.CharField(max_length=10, choices=UNIT_CHOICES)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)


class Rating(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    score = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    reviews = models.TextField(blank=True, null=True)


class Recomendation(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(blank=True, null=True)