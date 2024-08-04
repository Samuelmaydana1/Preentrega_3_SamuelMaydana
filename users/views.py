from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from users.forms import UserRegisterForm

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contrasenia)
            if user is not None:
                login(request, user)
                return redirect('Inicio')  # Redirige a una vista específica
        messages.error(request, 'Usuario o contraseña incorrectos')
    else:
        form = AuthenticationForm()
    
    return render(request, "users/login.html", {"form": form})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Inicio')
    else:
        form = UserRegisterForm()
    
    return render(request, "users/registro.html", {"form": form})