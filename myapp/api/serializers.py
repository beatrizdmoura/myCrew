from django.core.validators import MinLengthValidator
from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers
from api import models

class UserSerializer(serializers.ModelSerializer):
    """
    User Serializer
    """
    pass_style = {'input_type': 'password'}
    password = serializers.CharField(write_only=True, style=pass_style, validators=[MinLengthValidator(6)])
    confirm_password = serializers.CharField(write_only=True, required=False, style=pass_style)

    def create(self, validated_data):
        validated_data.pop('confirm_password', None)
        password = validated_data.pop('password')
        user = models.User(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def validate(self, data):
        if 'password' in data and ('confirm_password' not in data or data['password'] != data['confirm_password']):
            raise serializers.ValidationError({'confirm_password': _('Confirmation must match new password.')})
        return super(UserSerializer, self).validate(data)

    class Meta:
        model = models.User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'gender', 'profile_picture', 'password', 'confirm_password')
