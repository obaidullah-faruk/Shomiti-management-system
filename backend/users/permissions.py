from rest_framework.permissions import BasePermission


class IsMemberUser(BasePermission):
    """
    Access to Member type user
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and getattr(request.user, 'is_member', False))
