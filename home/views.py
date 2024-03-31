from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Animal, CustomUser

def animal(request):
    animals = Animal.objects.all()
    return render(request, 'Home.html', {'animals': animals})

def blogs(request):
    return render(request, 'blogs.html')

def farm(request):
    return render(request, 'farm.html')

def hospital(request):
    return render(request, 'hospital.html')

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Invalid Username')
            return redirect('/login/')
        
        user = authenticate(username=username, password=password)
        
        if user is None:
            messages.error(request, 'Invalid Password')
            return redirect('/login/')
        elif not user.is_active:
            messages.error(request, 'User is not active')
            return redirect('/login/')
        else:
            login(request, user)
            return redirect('/Home/')

    return render(request, 'login.html')

def Register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data.get('full_name')
            phone_number = form.cleaned_data.get('phone_number')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            CustomUser.objects.create(
                full_name=full_name,
                phone_number=phone_number,
                email=email,
                password=password
            )
            user = authenticate(email=email, password=password)
            login(request, user)
            return redirect('home') 
    else:
        form = UserCreationForm()
    return render(request, 'Register.html', {'form': form})

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
