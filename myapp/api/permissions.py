from rest_framework import permissions

def safe_request(request):
    return request.method in permissions.SAFE_METHODS

def requested_by_owner(request, obj):
    return obj == request.user

def not_authenticated_post(request):
    return request.method == "POST" and not request.user.is_authenticated

class CreateOwnerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it
    """

    def has_permission(self, request, view):
        return not_authenticated_post(request) or request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return safe_request(request) or requested_by_owner(request, obj)
