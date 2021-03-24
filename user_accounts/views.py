from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def registerview(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            try:
                user = User.objects.get(email=email)
                return render(request, 'user_accounts/register.html', {'error': 'Email address has already been registered!'})
            except User.DoesNotExist:
                user = User.objects.create_user(firstname, email, password1)
                user.first_name= firstname
                user.last_name= lastname
                user.save()
                login(request, user)
                return redirect('lms:homepage')
    else:
        return render(request, 'user_accounts/register.html')

def loginview(request):
    if request.method == 'GET':
        return render(request, 'user_accounts/login.html')
    elif request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']
        user = authenticate(request, username=name, password=password)
        if user is not None:
            login(request, user)
            return redirect('lms:homepage')
        else:
            return render(request, 'user_accounts/login.html', {'error':'The Email and Password didn\'t match'})

def logoutview(request):
    if request.method == 'POST':
        logout(request)
        return redirect('lms:homepage')
