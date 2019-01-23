from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404

from rest_framework import permissions
from rest_framework.decorators import list_route, permission_classes
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from api import models, serializers, pagination
from api import permissions as api_permissions

class UserViewSet(ModelViewSet):
    """
    User Viewset
    """
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [api_permissions.CreateOwnerOrReadOnly]
    pagination_class = pagination.ClientRequestedPagination

    @list_route(permission_classes=[permissions.AllowAny])
    def registered(self, request):
        return Response({
            'users_ids': self.queryset.values_list('id', flat=True),
            'count_female': self.queryset.filter(gender=models.User.FEMALE).count(),
            'count_male': self.queryset.filter(gender=models.User.MALE).count(),
            'count_unspecified': self.queryset.filter(gender=None).count()
        })
