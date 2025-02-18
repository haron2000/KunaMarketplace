from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from users.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from businesses.models import Business, Category
from .forms import CustomUserCreationForm, BusinessProfileForm

# Create your views here.
def signup_view(request):
    if request.method == "POST":
        user_form = CustomUserCreationForm(request.POST)
        business_form = BusinessProfileForm(request.POST, request.FILES)  # Always initialize
        
        if user_form.is_valid():
            user = user_form.save(commit=False)
            profile_type = user_form.cleaned_data.get("profile_type")
            user.profile_type = user_form.cleaned_data.get("profile_type")
            user.save()
            
            # If user is a business, create a BusinessProfile
            if profile_type == "business" and business_form.is_valid(): 
                    business = business_form.save(commit=False)
                    business.user = user
                    business.save()
                    
            login(request, user)
            return redirect("home")  # Redirect to homepage after signup

    else:
        user_form = CustomUserCreationForm()
        business_form = BusinessProfileForm()

    return render(request, "users/signup.html", {"user_form": user_form, "business_form": business_form})


def home(request):
    businesses = Business.objects.all() 
    categories = Category.objects.all()
    return render(request, 'users/home.html', {'businesses': businesses, 'categories': categories})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            if user.is_business:
                return redirect('businesses:create_profile')
            return redirect('users:home')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})
@login_required
def profile(request):
    return render(request, 'users/profile.html')

@property
def is_business(self):
    return self.profile_type == "business"
