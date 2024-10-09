from rest_framework import serializers
from .models import CustomUser, Dish, Ingredient, Rating, Recomendation


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = '__all__'

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'
    
class RecomendationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recomendation
        fields = '__all__'
    