from rest_framework import permissions


class AdminPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return False

        if request.user.role == 1:
            return True
        elif request.user.role == 2 or request.user.role == 3:
            return request.method in permissions.SAFE_METHODS
        return False


class UserPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return False

        if request.user.role == 2:
            return True
        elif request.user.role == 1 or request.user.role == 3:
            return request.method in permissions.SAFE_METHODS
        return False
