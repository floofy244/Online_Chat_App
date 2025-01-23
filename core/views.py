from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import SignUpForm
import logging

def frontpage(request):
    return render(request, 'core/frontpage.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            # Save the user
            user = form.save()
            
            # Explicitly log in the user
            login(request, user)
            
            # Add success message
            messages.success(request, 'Account created successfully!')
            
            # Print statements for debugging (remove in production)
            print("User created:", user.username)
            print("User is authenticated:", request.user.is_authenticated)
            
            # Redirect with full URL to ensure it works
            return redirect('/')  # or return redirect(reverse('frontpage'))
        else:
            # If form is not valid, add error messages
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field.capitalize()}: {error}")
            
            # Print form errors for debugging
            print("Form errors:", form.errors)
    else:
        form = SignUpForm()

    return render(request, 'core/signup.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('/')

    
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Validate input
        if not username or not password:
            messages.error(request, 'Please provide both username and password.')
            return render(request, 'core/login.html')
        
        # Authenticate user
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # User exists and credentials are correct
            login(request, user)
            messages.success(request, f'Welcome back, {username}!')
            return redirect('rooms')
        else:
            # Authentication failed
            messages.error(request, 'Invalid username or password. Please try again.')
    
    return render(request, 'core/login.html')