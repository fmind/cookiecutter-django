"""Object permissions of the project."""

from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """Permission to allow owners to edit their objects."""

    def has_object_permission(self, request, view, obj):
        """Check that owners can edit their objects."""
        # Read permissions are allowed to any request
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to owners
        return obj.owner == request.user
