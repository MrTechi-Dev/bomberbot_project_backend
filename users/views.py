""" User views """

# Local
from .serializers import LoginSerializer, SignupSerializer

# Django 
from django.contrib.auth.models import User

# RestFramework 
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status

class UserLogin(APIView):
    serializer_class = LoginSerializer
    permission_classes = (AllowAny,)
    http_method_names = ['post']
    
    def post(self, request):
        """ Post method to accepts the data 
        enclosed in the body of the request
        """
        
        serializer = self.serializer_class(data=request.data)
        
        # before attempting to access the validated data, or save an object instance
        if serializer.is_valid(raise_exception=True):
            status_code = status.HTTP_200_OK
            response = {
                'success': True,
                'status': status_code,
                'message': 'User login successful',
                'access': serializer.data['access'],
                'refresh': serializer.data['refresh'],
                'authenticatedUser': {
                    'username': serializer.data['username'],
                }   
            }
            return Response(response, status_code)

    
class UserSignup(APIView):
    serializer_class = SignupSerializer
    permission_classes = (AllowAny,)
    http_method_names = ['post']
    
    def post(self, request):
        """ Post method to accepts the data 
        enclosed in the body of the request
        """
        
        serializer = self.serializer_class(data=request.data)
        
        # before attempting to access the validated data, or save an object instance
        if serializer.is_valid(raise_exception=True):
            # .save() to return an object instance, based on the validated data
            # will create a new instance
            serializer.save()
            response = {
                'success': True,
                'status': status.HTTP_200_OK,
                'message': 'User registratition successful',
                'registered_user': serializer.data,
            }
            return Response(response, status.HTTP_200_OK) 
              
    