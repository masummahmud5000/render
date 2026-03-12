from rest_framework import serializers
from .models import Server, List
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
class ListCreateSerializer(serializers.Serializer):
    subject = serializers.CharField()
    text = serializers.CharField()

    def validate_subject(self, value):
        if len(value) > 20:
            raise serializers.ValidationError('subjectTextOnly20Char')
        else:
            return value
    
    def validate_text(self, value):
        if len(value) > 500:
            raise serializers.ValidationError('textOnly500Char')
        else:
            return value
        
    def create(self, validated_data):
        user = self.context['request'].user

        tudo = List.objects.create(
            user=user,
            subject=validated_data['subject'],
            textbox=validated_data['text']
        )

        return tudo
# /////////////////////////////////////////////////////////////////////
class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = ['id','subject','textbox','time']

class Patch(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = ['subject','textbox']