from rest_framework import serializers
from .models import Server
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
