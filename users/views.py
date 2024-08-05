from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from users.forms import UserRegisterForm, UserEditForm

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

@login_required
def editar_perfil(request):

    # El usuario para poder editar su perfil primero debe estar logueado.
    # Al estar logueado, podremos encontrar dentro del request la instancia
    # del usuario -> request.user
    usuario = request.user

    if request.method == 'POST':

        miFormulario = UserEditForm(request.POST, instance=request.user)

        if miFormulario.is_valid():

            miFormulario.save()

            # Retornamos al inicio una vez guardado los datos
            return render(request, "AppSamuel/index.html")

    else:
        miFormulario = UserEditForm(instance=request.user)

    return render(
        request,
        "users/editar_perfil.html",
        {
            "mi_form": miFormulario,
            "usuario": usuario
        }
    )

class CambiarPassView(LoginRequiredMixin, PasswordChangeView):

    template_name = "users/cambiar_pass.html"
    success_url = reverse_lazy('Inicio')