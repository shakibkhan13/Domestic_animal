from django.shortcuts import render, redirect
from .models import Animal
from django.contrib.auth.models import User

def animal(request):
    animals = Animal.objects.all()
    return render(request, 'Home.html', {'animals': animals})


def blogs(request):
    return render(request, 'blogs.html')

def farm(request):
    return render(request, 'farm.html')


def hospital(request):
    return render(request, 'hospital.html')

def login(request):
    return render(request, 'login.html')

def Register(request):
    if request.method == "POST":
       full_name = request.POST.get('full_name')
       Phone_number = request.POST.get('Phone_number')
       Email_Address = request.POST.get('Email_Address')
       password = request.POST.get('password')
       
       user = User.objects.create_user(
           username=Email_Address,
           email=Email_Address,
           password=password,
           full_name=full_name,
           phone_number=Phone_number,
       )

    return render(request, 'Register.html')

def seller(request):
    if request.method == "POST":
        data = request.POST
        Animal_name = data.get('Animal_name')
        Animal_Weight = data.get('Animal_Weight')
        Animal_Prize = data.get('Animal_Prize')
        Animal_Farm = data.get('Animal_Farm')
        Animal_description = data.get('Animal_description')
        Animal_image = request.FILES.get('Animal_image')

        Animal.objects.create(
            Animal_name=Animal_name,
            Animal_Weight=Animal_Weight,
            Animal_Prize=Animal_Prize,
            Animal_Farm=Animal_Farm,
            Animal_description=Animal_description,
            Animal_image=Animal_image
        )

        return redirect('/seller/')

    queryset = Animal.objects.all()
    context = {'seller':queryset}
    return render(request, 'seller.html',context)
def delete_animal(request ,id): 
    queryset = Animal.objects.get(id=id)
    queryset.delete()
    return redirect('/seller/')

def cart(request):
    return render(request, 'cart.html')

def maps(request):
    return render(request, 'maps.html')
