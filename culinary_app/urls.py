from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, DishViewSet, IngredientViewSet, RatingViewSet, RecomendationViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'dishes', DishViewSet)
router.register(r'ingredients', IngredientViewSet)
router.register(r'ratings', RatingViewSet)
router.register(r'recomendations', RecomendationViewSet)


urlpatterns = [
    path('', include(router.urls))
]