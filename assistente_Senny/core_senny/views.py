from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Cadastro


def cadastro_usuario(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid:
            user = form.save()

            Cadastro.objects.create(usuario=user)

            messages.success(
                request, f"Usuário Criado para {user.username} faça seu login."
            )
            return redirect("login_usuario")
        else:
            pass
    else:
        form = UserCreationForm()

    return render(request, "cadastro.html", {"form": form})


def login_usuario(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, f"Bem-vindo(a) de volta, {user.username}!")
                return redirect("dashboard_usuario")
            else:

                messages.error(
                    request,
                    "Nome de usuário ou senha inválidos. Por favor, tente novamente.",
                )

        else:

            pass

    else:
        form = AuthenticationForm()

    return render(request, "login.html", {"form": form})


def dashboard(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Você precisa estar logado para acessar esta página.")
        return redirect("login.html")

    return render(request, "dashboard.html")


def logout_usuario(request):
    logout(request)
    messages.info(request, "Você foi desconectado.")

    return redirect("login.html")
