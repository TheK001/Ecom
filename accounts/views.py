from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm, LoginForm
from .models import CustomUser
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful. Please log in.")
            return redirect('login')
    else:
        form = RegisterForm()
    context = {
            'form': form,
        }

    return render(request, 'registration/register.html', context)

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)  # Authenticate using email
            if user is not None:
                login(request, user)
                messages.success(request, 'Logged in successfully!')
                return redirect('home')  # Redirect to the home page
            else:
                messages.error(request, 'Invalid email or password.')  # Show error message
    else:
        form = LoginForm()
    context = {
        'form': form,
    }
    return render(request, 'registration/login.html', context)

def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('login')  

def list_users(request):
    users = CustomUser.objects.all()
    context = {
        'users': users,
    }
    return render(request, 'user_list.html', context)