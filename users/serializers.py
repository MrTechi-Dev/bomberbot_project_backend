""" Serializer for User views """

from rest_framework import serializers
from django.contrib.auth.models import User

#prueba

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')



class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 
                  'password', 
                  'password', 
                  'first_name', 
                  'last_name', 
                  'email')

# class LoginSerializer(serializers.ModelSerializer):
#     """ Serializer for login endpoint """
#     class Meta:
#         model = User
#         fields = ['username', 'password']
