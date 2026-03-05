from rest_framework import serializers
from .models import Server
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
# ////////////////////////////
# //////////////////////////  Sing Up  //////////////////////////////
class SingupSerializer(serializers.Serializer):
    name = serializers.CharField()
    username = serializers.CharField()
    password = serializers.CharField()

    def validate_username(self, value):
        already = Server.objects.filter(username=value)

        if already.exists():
            raise serializers.ValidationError('userAlreadyExists')
        elif len(value) < 8:
            raise serializers.ValidationError('usernameNotStrong')
        
        return value
    
    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError('passwordNotStrong')
        else:
            return value
    
    def create(self, validated_data):
        user = Server.objects.create_user(**validated_data)
        return user
# /////////////////////////////////////////////////////////////////////
class SignInSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):

        username = attrs['username']
        password = attrs['password']

        user = authenticate(username=username, password=password)
        
        if not user:
            raise serializers.ValidationError('userNotFound')
        else:
            refresh = RefreshToken.for_user(user)
            attrs['refresh'] = str(refresh)
            attrs['access'] = str(refresh.access_token)
            attrs['user'] = str(user.username)

            return attrs
# /////////////////////////////////////////////////////////////////////