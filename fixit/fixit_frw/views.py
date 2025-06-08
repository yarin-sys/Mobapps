# fixit_frw/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import CustomUserCreationForm, RepairRequestForm
from .models import RepairRequest, ItemImage

def landing_page_view(request):
    # Now, render the landing page template from the app's templates directory
    return render(request, "landing/index.html")

def user_login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, "Login berhasil!")
            return redirect(reverse('menu_page'))
        else:
            messages.error(request, "Username atau password salah.")
    return render(request, "registration/login.html")

def user_logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect(reverse('landing_page'))

def authView(request): # This is the signup view
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registrasi berhasil! Silakan login.")
            return redirect(reverse('login'))
        else:
            messages.error(request, "Registrasi gagal. Periksa kembali data Anda.")
    else:
        form = CustomUserCreationForm()
    return render(request, "registration/signup.html", {"form": form})

@login_required #menupage item requests
def menu_page_view(request):
    repair_requests = RepairRequest.objects.all().order_by('-created_at')
    return render(request, 'menupage.html', {'repair_requests': repair_requests})

@login_required
def product_details_views(request):
    return render(request, 'ProductDetails.html')

@login_required
def chat_page_views(request):
    return render(request, 'chatpage.html')

@login_required
def fixit_success_view(request):
    return render(request, 'fixit_success_page.html')

@login_required
def upload_item_view(request):
    if request.method == 'POST':
        form = RepairRequestForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                repair_request = form.save(commit=False)
                # repair_request.user = request.user # If you add a user foreign key to RepairRequest
                repair_request.save()
                images = request.FILES.getlist('images')
                if len(images) > 10:
                    messages.error(request, "You can upload a maximum of 10 images.")
                    return render(request, 'uploadpage.html', {'form': form})
                for file_instance in images:
                    if file_instance:
                         ItemImage.objects.create(request=repair_request, image=file_instance)
                messages.success(request, "Item berhasil diunggah!")
                return redirect(reverse('upload_success'))
            except Exception as e:
                messages.error(request, f"Terjadi kesalahan saat mengunggah: {e}")
        else:
            messages.error(request, "Form tidak valid. Periksa kembali data Anda.")
    else:
        form = RepairRequestForm()
    return render(request, 'uploadpage.html', {'form': form})

@login_required
def upload_success_view(request):
    return render(request, 'success_page.html')

# --- repairrequest models ---
@login_required
def repairrequest_list(request):
    repair_requests = RepairRequest.objects.all()
    return render(request, 'repairrequest_list.html', {'repair_requests': repair_requests})

# --- repairrequest models ---
def repairrequest_detail(request, pk):
    repair_request = get_object_or_404(RepairRequest, pk=pk)
    return render(request, 'ProductDetails.html', {'repair_request': repair_request})

# --- Update these other placeholder views similarly if you want Django to serve them ---
def confirmation_page_view(request, item_id):
    item = get_object_or_404(RepairRequest, pk=item_id)
    # Assuming confirmationPage/index.html is moved to templates/confirmationPage/index.html
    # and its assets to static/confirmationPage/
    return render(request, "confirmationPage/index.html", {'item': item})

def maps_page_view(request):
    # Assuming maps/index.html is moved to templates/maps/index.html
    # and its assets to static/maps/
    return render(request, "maps/index.html")

def history_page_view(request):
    # Assuming history/index.html is moved to templates/history/index.html
    # and its assets to static/history/
    # return render(request, "history/index.html")
    # For now, if history.html is very simple or not ready:
    from django.http import HttpResponse
    return HttpResponse("History page placeholder. Move history/index.html to templates and update view.")
