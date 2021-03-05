# Django
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

# Create your views here.

def login_view(request):
    """Login view."""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home/home')
        else:
            return render(request, 'users/login.html', {'error': 'Invalid username and password'})

    return render(request, 'users/login.html')

@login_required
def logout_view(request):
    """Logout a user."""
    logout(request)
    return redirect('users/login')
