from locale import currency
from re import A
import re
from rest_framework import serializers, viewsets, views
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render
from .forms import agregarcliFrom, registrarForm, perfilForm

# Create your views here.


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializers


class PlantillaViewSet(viewsets.ModelViewSet):
    queryset = Plantilla.objects.all()
    serializer_class = PlantillaSerializers


class SolicitudViewSet(viewsets.ModelViewSet):
    queryset = Solicitud.objects.all()
    serializer_class = SolicitudSerializers


class DocumentoViewSet(viewsets.ModelViewSet):
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializers


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializers


class AbogadoViewSet(viewsets.ModelViewSet):
    queryset = Abogado.objects.all()
    serializer_class = AbogadoSerializers


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {"form": AuthenticationForm})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {"form": AuthenticationForm, "error": "Username or password is incorrect."})

        login(request, user)
        return redirect(to='ahome')


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {"form": registrarForm})
    else:

        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    request.POST["username"],
                    password=request.POST["password1"],
                    first_name=request.POST['first_name'],
                    last_name=request.POST['last_name'],
                    email=request.POST['email'])
                group = Group.objects.get(name='cliente')
                user.groups.add(group)
                user.save()
                login(request, user)
                return redirect('ahome')
            except IntegrityError:
                return render(request, 'signup.html', {"form": registrarForm, "error": "Usuario ya existe."})

        return render(request, 'signup.html', {"form": UserCreationForm, "error": "Contrasenias no coinciden."})


@login_required
def signout(request):
    logout(request)
    return redirect('ahome')


@login_required
def ahome(request):
    clientes = Cliente.objects.filter(user=request.user)
    user = User.objects.filter(username=request.user)
    data = {
        'user':user
        # 'clientes': clientes
    }
    return render(request, 'ahome.html', data)


@login_required
def agregarcli(request):
    if request.method == 'GET':
        return render(request, 'agregarcli.html', {
            'form': registrarForm
        })
    else:
        try:
            form = registrarForm(request.POST)
            nuevocli = form.save(commit=False)
            nuevocli.user = request.user
            nuevocli.save()
            messages.success(request, "Cliente Agregado")
            return redirect('ahome')
        except ValueError:
            return render(request, 'gregarcli.html', {
                'form': registrarForm,
                'error': 'Por favor ingrese datos valida'
            })


# @login_required
# def modificarcli(request, id):
#     cliente = get_object_or_404(Cliente, id=id)

#     data = {
#         'form': agregarcliFrom(instance=cliente)
#     }

#     if request.method == 'POST':
#         formulario = agregarcliFrom(
#             data=request.POST, instance=cliente, files=request.FILES)
#         if formulario.is_valid():
#             formulario.save()
#             messages.success(request, "Cliente modificado Correctamente")
#             return redirect(to='ahome')
#         data['form'] = formulario

#     return render(request, 'modificarcli.html', data)



@login_required
def eliminarcli(request, username):
    user = get_object_or_404(User, username=username)
    user.delete()
    messages.success(request, "Cliente eliminado correctamente")
    return redirect(to='ahome')


def miperfil(request, username=None):
    current_user = request.user
    if username and username != current_user.username:
        user = User.objects.get(username=username)
    else:
        user = current_user
    return render(request, 'miperfil.html', {'user': user})


def modificarperfil(request,username=None):
    perfil = get_object_or_404(Perfil, user=username)

    data = {
        'form': perfilForm(instance=perfil)
    }

    if request.method == 'POST':
        formulario = perfilForm(
            data=request.POST, instance=perfil, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Perfil modificado Correctamente")
            return redirect(to='ahome')
        data['form'] = formulario
    return render(request, 'modificarperfil.html',data)

@login_required
def modificarcli(request, username):
    user = get_object_or_404(User, username=username)

    data = {
        'form': registrarForm(instance=user)
    }

    if request.method == 'POST':
        formulario = registrarForm(
            data=request.POST, instance=user, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Cliente modificado Correctamente")
            return redirect(to='ahome')
        data['form'] = formulario

    return render(request, 'modificarcli.html', data)