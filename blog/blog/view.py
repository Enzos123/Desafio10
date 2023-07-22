from django.shortcuts import render

def index(request):
    return render(request, 'index.html');

def noticia(request):
    return render(request, "noticia.html");
