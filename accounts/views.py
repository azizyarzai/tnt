from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib import messages
from django.urls import reverse_lazy

User = get_user_model()

# Create your views here.


def login_user(request):
    if request.user.is_authenticated:
        return redirect(reverse_lazy('students:list'))
    if request.method == 'GET':
        return render(request, 'accounts/login.html')
    else:
        email = request.POST.get("email")
        password = request.POST.get("password")

        # try:
        #     user = User.objects.get(email=email)

        #     if not user.check_password(password):
        #         raise User.DoesNotExist("Does not exist")
        #     print("user", user)
        # except User.DoesNotExist:
        #     messages.error(request, 'Invalid Credentials.')
        #     return render(request, 'accounts/login.html')

        user = authenticate(email=email, password=password)
        print(user)
        if user:
            login(request, user)
            return redirect(reverse_lazy('students:list'))
        else:
            messages.error(request, 'Invalid Credentials.')
            return render(request, 'accounts/login.html')


def register_user(request):
    if request.user.is_authenticated:
        return redirect(reverse_lazy('students:list'))
    if request.method == 'GET':
        return render(request, 'accounts/register.html')
    else:
        email = request.POST.get("email")
        pass1 = request.POST.get("pass1")
        pass2 = request.POST.get("pass2")
        phone = request.POST.get("phone")
        name = request.POST.get("name")

        user = authenticate(email=email)
        if user:
            messages.warning(request, 'Email already exists.')
            return redirect(reverse_lazy("accounts:register"))

        if pass1 != pass2:
            messages.warning(request, 'Passwords did not match.')
            return redirect(reverse_lazy("accounts:register"))

        user = User.objects.create_user(
            name=name, email=email, password=pass1, phone=phone)
        messages.success(request, 'user created successfuly.')
        return redirect(reverse_lazy("accounts:login"))


def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect(reverse_lazy('students:list'))
