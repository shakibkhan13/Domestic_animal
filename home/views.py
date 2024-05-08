
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
from .models import Customer

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
    if request.method == "POST":
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
        Customer.objects.create(user=user)
        
        messages.success(request, 'Account created successfully')
        return redirect('/login/')

    return render(request, 'register.html')

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
    if request.user.is_authenticated:
        try:
            customer = request.user.customer
        except Customer.DoesNotExist:
            messages.error(request, 'Please register to access the cart.')
            return redirect('/register/') 

        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'cart.html', context)



def maps(request):
    return render(request, 'maps.html')

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
        cartItems = order['get_cart_items']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'checkout.html', context)




def update_item(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('Product:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)