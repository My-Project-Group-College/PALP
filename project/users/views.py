from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from courses.models import Course
from conversations.models import Conversation

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')  # Redirect to dashboard after login
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')  # Redirect to dashboard after signup
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def dashboard_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    courses = Course.objects.filter(creator=request.user)
    conversations = Conversation.objects.filter(user=request.user)
    
    return render(request, 'dashboard.html', {
        'courses': courses,
        'conversations': conversations
    })