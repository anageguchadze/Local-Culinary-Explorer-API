from rest_framework import permissions
from .models import CustomUser

class IsChef(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == CustomUser.CHEF
    

