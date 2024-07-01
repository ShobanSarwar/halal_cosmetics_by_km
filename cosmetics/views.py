from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.cache import never_cache
from .forms import CustomUserCreationForm
from .models import Product
from .forms import ProductForm


@never_cache
@login_required
def home(request):
    products = Product.objects.all()
    return render(request, 'cosmetics/home.html', {'products': products})


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProductForm()
    return render(request, 'cosmetics/add_product.html', {'form': form})


def product_detail(request, product_id):
    product = Product.objects.get(pk=product_id)
    return render(request, 'cosmetics/product_detail.html', {'product': product})


@never_cache
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'cosmetics/login.html', {'form': form})


@never_cache
def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after signup
            return redirect('home')  # Redirect to home page after signup
    else:
        form = CustomUserCreationForm()
    return render(request, 'cosmetics/signup.html', {'form': form})


def about(request):
    return render(request, 'cosmetics/about.html')


def contact(request):
    return render(request, 'cosmetics/contact.html')


def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('home')
    return render(request, 'cosmetics/delete_product.html', {'product': product})
