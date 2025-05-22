from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import CustomUserCreationForm
from .forms import RepairRequestForm
from .models import RepairRequest, ItemImage

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, "Login berhasil")
            return redirect("http://localhost:8000/")  # Ganti dengan halaman tujuan setelah login
        else:
            messages.error(request, "Username atau password salah")

    return render(request, "login.html")

def authView(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('http://localhost:8000/accounts/login/')
    else:
        form = CustomUserCreationForm()
    return render(request, "registration/signup.html", {"form" : form})

def menu_page(request):
    return render(request, 'menupage.html')

def upload_page(request):
    return render(request, 'uploadpage.html')

def upload_item(request):
    if request.method == 'POST':
        form = RepairRequestForm(request.POST)
        if form.is_valid():
            repair_request = form.save()
            # Handle multiple images
            for file in request.FILES.getlist('images'):
                ItemImage.objects.create(request=repair_request, image=file)
            return redirect('success_page')  # Replace with your actual success view
    else:
        form = RepairRequestForm()

    return render(request, 'uploadpage.html', {'form': form})
