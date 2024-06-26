
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Animal, Order, ShippingAddress
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from .models import Customer, Animal
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse

def home(request):
    animals = Animal.objects.all()
    return render(request, 'home.html', {'animals': animals})

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
        
        else:
            login(request, user)
            return redirect('/home/')

    return render(request, 'login.html')

def logout_page(request):
    logout(request)
    return redirect('/login/')

#@login_required(login_url="/login/")
def blogs(request):
    animals = Animal.objects.all()
    return render(request, 'blogs.html')

#login_required(login_url="/login/")
def farm(request):
    return render(request, 'farm.html')

@login_required(login_url="/login/")
def hospital(request):
    return render(request, 'hospital.html')

def Register(request):
    if request.method != "POST":
        return render(request, 'register.html')   
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    username = request.POST.get('username')
    password = request.POST.get('password')

    if not username:  
        return redirect('/register/') 

    user = User.objects.filter(username=username)

    if user.exists():
        messages.error(request, 'Username already taken')
        return redirect('/register/')

    user = User.objects.create_user(
        username=username,
        password=password,
        first_name=first_name,
        last_name=last_name,
    )
    user.save()
    messages.success(request, 'Account created successfully')
    return redirect('/register/')

@login_required(login_url="/login/")
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
    context = {'seller': queryset}
    return render(request, 'seller.html', context)

def delete_animal(request ,id): 
    queryset = Animal.objects.get(id=id)
    queryset.delete()
    return redirect('/seller/')


@login_required(login_url="/login/")
def cart(request):
    try:
        customer = request.user.customer
    except Customer.DoesNotExist:
        customer = None  
    animals = Animal.objects.all()
    total_price = sum(animal.Animal_Prize for animal in animals)
    return render(request, 'cart.html', {'customer': customer, 'animals': animals, 'total_price': total_price})



def maps(request):
    return render(request, 'maps.html')

def checkout(request):
    # try:
    #     customer = request.user.customer
    # except Customer.DoesNotExist:
    #     customer = None  
    # animals = Animal.objects.all()
    # total_price = sum(animal.Animal_Prize for animal in animals)
    try:
        customer = request.user.customer
    except Customer.DoesNotExist:
        customer = None  
    animals = Animal.objects.all()
    total_price = sum(animal.Animal_Prize for animal in animals)
    return render(request, 'checkout.html', {'customer': customer, 'animals': animals, 'total_price': total_price})


def update_item(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Method not allowed'}, status=405)
    data = request.POST
    product_id = data.get('productId')
    action = data.get('action')
    return JsonResponse({'message': 'Item updated successfully'}, status=200)