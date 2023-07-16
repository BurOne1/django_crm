from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.

def index(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        # auth
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Вы вошли в систему")
            return redirect('main')
        else:
            messages.success(request, "Произошла ошибка")
            return redirect('main')
    else:
        return render(request, 'main/login_page.html')




def logout_user(request):
    pass
