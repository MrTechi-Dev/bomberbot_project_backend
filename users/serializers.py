""" Serializer for User views """
# Django
from django.contrib.auth.models import User

# RestFramework Django
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import update_last_login
from django.contrib.auth import authenticate


class LoginSerializer(serializers.Serializer):
    """ Serializer for Login view """
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100, write_only=True)
    refresh = serializers.CharField(read_only=True)
    access = serializers.CharField(read_only=True)


    def validate(self, data):
        """ Validates username and password """
        username = data['username']
        password = data['password']
        user = authenticate(username=username, 
                            password=password)
        if user:
            try:
                refresh = RefreshToken.for_user(user)
                refresh_token = str(refresh)
                access_token = str(refresh.access_token)
                
                update_last_login(None, user)
                
                validate = {
                    'access': access_token,
                    'refresh': refresh_token,
                    'username': user.username,
                    'password': user.password,
                }
                return validate
            except User.DoesNotExist:
                raise serializers.ValidationError('Invalid username/password')
        raise serializers.ValidationError('Invalid username/password')


class SignupSerializer(serializers.ModelSerializer):
    """ Serializer User Signup """
    class Meta:
        model = User
        fields = (
            'username', 
            'password', 
            'password', 
            'first_name', 
            'last_name', 
            'email'
        )
    
    def create(self, validated_data):
        """ 
        Creates a new User
        Returns:
            complete object instances based on the validated data we need
        """
        return User.objects.create_user(**validated_data)

class ChangePasswordSerializer(serializers.Serializer):
    model = User

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)