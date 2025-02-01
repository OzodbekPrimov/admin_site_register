from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

def login_required_decorator(func):
    return login_required(func, login_url='login_page')

@login_required_decorator
def logout_page(request):
    logout(request)
    return redirect("login_page")


def login_page(request):
    if request.POST:  # 1️⃣ Agar POST so‘rov bo‘lsa (foydalanuvchi formani yuborsa)
        username = request.POST.get('username')  # 2️⃣ Foydalanuvchidan 'username' ni olish
        password = request.POST.get('password')  # 3️⃣ Foydalanuvchidan 'password' ni olish
        user = authenticate(request, password=password, username=username)  # 4️⃣ Foydalanuvchini tekshirish

        if user is not None:  # 5️⃣ Agar foydalanuvchi mavjud bo‘lsa
            login(request, user)  # 6️⃣ Foydalanuvchini tizimga kiritish
            return redirect("home_page")  # 7️⃣ Uni "home_page" sahifasiga yo‘naltirish

    return render(request, 'login.html')  # 8️⃣ Agar POST so‘rov bo‘lmasa, "login.html" sahifasini ko‘rsatish


def home_page(request):
    return render(request, 'index.html')


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login_page')
    template_name = 'signup.html'