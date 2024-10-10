from rest_framework import permissions
from .models import CustomUser

class IsChef(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == CustomUser.CHEF
    

class CanAddRecipe(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.role == CustomUser.USER