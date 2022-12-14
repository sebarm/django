from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'modulo1/home.html');

def tienda(request):
    return render(request, 'modulo1/tienda.html');

def historia(request):
    return render(request, 'modulo1/historia.html');