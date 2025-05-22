from django import forms
from .models import RepairRequest
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "phone", "address", "password1", "password2")


class RepairRequestForm(forms.ModelForm):
    class Meta:
        model = RepairRequest
        fields = ['item_name', 'description', 'pickup_address', 'offer_price']
