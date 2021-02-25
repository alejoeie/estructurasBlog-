from django.shortcuts import render, HttpResponse
from home import models
# Create your views here.

def home(request):
    # return HttpResponse('This is my homepage (/)')
    context = {'name': 'Alejandro', 'course': 'Django'}
    return render(request, 'home.html', context)

def about(request):
    # return HttpResponse('This is my about page (/about)')
    return render(request, 'about.html')

def projects(request):
    # return HttpResponse('This is my projects page (/projects)')
    return render(request, 'projects.html')

def enthusiasts(request):
    return render(request, 'enthusiasts.html')

def curriculum(request):
    return render(request, 'curriculum.html')
    
def method(request):
    return render(request, 'method.html')
def detector(request):
    return render(request, 'detector.html')

def contact(request):
    if request.method == "POST":
        print("Se ha enviado correctamente")
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        desc=request.POST['desc']
        # print(name,email,phone,desc)
        contact = models.Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        print("Los datos han sido escritos a la base de datos")
    # return HttpResponse('This is my contact page (/contact)')
    return render(request, 'contact.html')