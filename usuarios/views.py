from django.shortcuts import render

def login(request):
    return render("usuarios/login.html")

def cadastro(request):
    return render("usuarios/cadastro.html")
