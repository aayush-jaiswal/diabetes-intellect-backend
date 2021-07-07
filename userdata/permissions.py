from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """
    Custom permissions to only allow owner of data to access it
    """

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user
