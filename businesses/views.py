from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from  .models import Business, BusinessImage
from businesses.forms import BusinessProfileForm, BusinessImageForm

@login_required
def create_business_profile(request):
    if hasattr(request.user, 'business'):
        messages.warning(request, 'You already have a business profile')
        return redirect('businesses:business_profile')
        
    if request.method == 'POST':
        form = BusinessProfileForm(request.POST)
        image_form = BusinessImageForm(request.POST, request.FILES)
        
        if form.is_valid() and image_form.is_valid():
            business = form.save(commit=False)
            business.owner = request.user
            business.save()
            
            if 'image' in request.FILES:
                image = image_form.save(commit=False)
                image.business = business
                image.is_primary = True
                image.save()
                
            messages.success(request, 'Business profile created successfully!')
            return redirect('businesses:business_profile')
    else:
        form = BusinessProfileForm()
        image_form = BusinessImageForm()
    
    return render(request, 'businesses/create_profile.html', {
        'form': form,
        'image_form': image_form
    })

@login_required
def business_profile(request):
    business = Business.objects.filter(owner=request.user).first()
    return render(request, 'businesses/business_profile.html', {'business': business})

@login_required
def edit_business_profile(request):
    business = get_object_or_404(Business, owner=request.user)
    
    if request.method == 'POST':
        form = BusinessProfileForm(request.POST, instance=business)
        if form.is_valid():
            form.save()
            messages.success(request, 'Business profile updated successfully!')
            return redirect('business_profile')
    else:
        form = BusinessProfileForm(instance=business)
    
    return render(request, 'businesses/edit_profile.html', {'form': form})

def business_list(request):
    businesses = Business.objects.prefetch_related('images').all()
    return render(request, 'businesses/list.html', {'businesses': businesses})

def business_detail(request, business_id):
    business = get_object_or_404(Business, id=business_id)
    return render(request, 'businesses/detail.html', {'business': business, 'chat_room': business.chat_room})


