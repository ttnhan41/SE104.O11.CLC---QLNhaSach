from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User


# Dang nhap
def loginUser(request):
    
    if request.user.is_authenticated:
        return redirect('bookstore')
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exists')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('bookstore')
        else:
            messages.error(request, 'Username or password is incorrect')

    return render(request, 'users/login.html')


# Dang xuat
def logoutUser(request):
    logout(request)
    messages.success(request, 'User was logged out!')
    return redirect('login')


# Mo trang thong tin nha sach
def bookstore(request):
    return render(request, 'users/bookstore-info.html')