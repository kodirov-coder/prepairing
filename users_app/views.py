from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import UserLoginForm, UserRegisterForm, ProfileForm
from products_app.models import Basket

def login_view(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            print("1-if ishladi")
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('products:main-page'))
    else:
        form = UserLoginForm()
    context = {
        'form': form
    }
    return render(request, "users/login.html", context)

def register_view(request):
    if request.method == "POST":
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Siz muvaffaqiyatli tarzda ro'yxatdan o'tdingiz!")
            return HttpResponseRedirect(reverse("users:login"))
    else:
        form = UserRegisterForm()
    context = {
        "form": form
    }
    return render(request, "users/register.html", context)

def profile_view(request):
    if request.method == "POST":
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Ma'lumotlar yangilandi!")
            return HttpResponseRedirect(reverse("users:profile"))
        else:
            print(form.errors)
    else:
        form = ProfileForm(instance=request.user)
    context = {
        "form": form,
        "baskets": Basket.objects.filter(user=request.user)
    }
    return render(request, "users/profile.html", context)

def logout_view(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse("products:main-page"))