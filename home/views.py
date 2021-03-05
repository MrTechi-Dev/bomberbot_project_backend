# Django
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Utilities
from datetime import datetime

# Create your views here.

@login_required
def home(request):
    """List existing posts."""
    return render(request, 'home/home.html')