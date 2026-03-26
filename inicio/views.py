from django.shortcuts import render

def index(request):
    return render(request, 'inicio/index.html')

def contacto(request):
    enviado = False
    if request.method == 'POST':
        enviado = True
    return render(request, 'inicio/index.html', {'enviado': enviado})