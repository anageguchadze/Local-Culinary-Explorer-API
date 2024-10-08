from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
UNIT_CHOICES = [
    ('g', 'gram'),
    ('kg', 'kilogram'),
    ('l', 'liter'),
    ('ml', 'milliliter'),
    ('pcs', 'piece'),
]

class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    joined_date = models.DateTimeField(auto_now_add=True)
    is_chef = models.BooleanField()


class Chef(models.Model):
    user = models.CharField(max_length=100)
    bio = models.TextField()
    speciality = models.CharField(max_length=100)
    profile_picture = models.URLField(max_length=200)


class Dish(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    preparation_method = models.TextField()
    image = models.URLField(max_length=200)
    chef = models.ForeignKey(Chef, on_delete=models.CASCADE)
    created_at = models.DateTimeField()
    updated_at = models.DateField(auto_now_add=True)

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.FloatField()
    unit = models.CharField(max_length=10, choices=UNIT_CHOICES)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    score = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    reviews = models.TextField(blank=True, null=True)


class Recomendation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(blank=True, null=True)