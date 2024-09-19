from rest_framework import serializers

from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth import get_user_model

from .models import CustomUser


class CustomTokenObtainSerializer(serializers.Serializer):
    # Use email for generate token
    # Remove the password field

    username_field = get_user_model().EMAIL_FIELD

    def __init__(self, *args, **kwargs):
        super(CustomTokenObtainSerializer, self).__init__(*args, **kwargs)

        self.fields[self.username_field] = serializers.EmailField()

    def validate(self, attrs):
        self.user = CustomUser.objects.filter(email=attrs[self.username_field]).first()

        if not self.user:
            raise serializers.ValidationError('Invalid user email.')

        return {}

    @classmethod
    def get_token(cls, user):
        raise NotImplemented(
            'Must implement `get_token` method for `MyTokenObtainSerializer` subclasses')


class CustomTokenObtainPairSerializer(CustomTokenObtainSerializer):
    @classmethod
    def get_token(cls, user):
        return RefreshToken.for_user(user)

    def validate(self, attrs):
        data = super(CustomTokenObtainPairSerializer, self).validate(attrs)

        refresh = self.get_token(self.user)

        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        return data
