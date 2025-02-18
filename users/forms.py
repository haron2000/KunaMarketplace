from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, BusinessProfile

class CustomUserCreationForm(UserCreationForm):
    profile_type = forms.ChoiceField(
        choices=User.PROFILE_TYPE_CHOICES, 
        widget=forms.RadioSelect
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'profile_type', 'password1', 'password2']

class BusinessProfileForm(forms.ModelForm):
    class Meta:
        model = BusinessProfile
        fields = ['business_name', 'location', 'photos']
