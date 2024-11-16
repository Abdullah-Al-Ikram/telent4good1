from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import VolunteerSignUpForm, OrganizationSignUpForm
# Create your views here.

def register(request):
    return render(request, 'register.html')

def volunteer_register(request):
    if request.method == 'POST':
        v_form = VolunteerSignUpForm(request.POST)
        if v_form.is_valid():
            user = v_form.save()
            login(request, user)
            messages.success(request, "Volunteer registered successfully!")
            return redirect('/')
    else:
        v_form = VolunteerSignUpForm()
    return render(request, 'volunteer_register.html', {'form': v_form})

def organization_register(request):
    if request.method == 'POST':
        o_form = OrganizationSignUpForm(request.POST)
        if o_form.is_valid():
            user = o_form.save()
            login(request, user)
            messages.success(request, "Organization registered successfully!")
            return redirect('/')
    else:
        o_form = OrganizationSignUpForm()
    return render(request, 'organization_register.html', {'form': o_form})

def login_user(request):
    if request.method == 'POST':
        log_form = AuthenticationForm(request, data=request.POST)
        if log_form.is_valid():
            username = log_form.cleaned_data.get('username')
            password = log_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome back, {user.username}!")
                #messages.success(request, "You are now logged in!")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    log_form = AuthenticationForm()
    return render(request, 'login.html', {'form': log_form})

def logout_user(request):
    logout(request)
    messages.success(request, "You are now logged out!")
    return redirect('/')