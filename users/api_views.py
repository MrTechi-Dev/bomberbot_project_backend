""" Exposing User API's """

# Django 
from django.contrib.auth.models import User
from django.views import View
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


# RestFramework 
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .serializers import LoginSerializer, SignupSerializer
from rest_framework import viewsets
from rest_framework import generics

class UserLogin(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = LoginSerializer


    
class UserSignup(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignupSerializer