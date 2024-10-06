from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'home.html')

def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Invalid username.')
            return redirect('/auth/login/')
        
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/auth/home/')
        else:
            messages.error(request, 'Invalid password.')
            return redirect('/auth/login/')

    elif request.method != 'GET':
        messages.error(request, 'Invalid request method.')

    return render(request, 'login.html')


def register_page(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return redirect('/auth/register/')
        
        if password != password2:
            messages.error(request, 'Passwords do not match.')
            return redirect('/auth/register/')
        
        user = User.objects.create_user(
            username=username, 
            first_name=first_name,
            last_name=last_name,
        )
        user.set_password(password)
        user.save()
        messages.success(request, 'User created successfully.')
        return redirect('/auth/home/')

    elif request.method != 'GET':
        messages.error(request, 'Invalid request method.')

    return render(request, 'register.html')
