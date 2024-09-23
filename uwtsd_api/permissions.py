from rest_framework.permissions import BasePermission

class IsSuperUser(BasePermission):
    """
    Custom permission to only allow superusers to edit objects.
    
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_superuser
