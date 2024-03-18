from django.shortcuts import render
from .models import Animal

def animal(request):
    return render(request, 'Home.html')

def blogs(request):
    return render(request, 'blogs.html')

def farm(request):
    return render(request, 'farm.html')

def Home(request):
    return render(request, 'Home.html')

def hospital(request):
    return render(request, 'hospital.html')

def login(request):
    return render(request, 'login.html')

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
    else:
        return render(request, 'seller.html')

    return render(request, 'seller.html')

def cart(request):
    return render(request, 'cart.html')
