from django import forms
from .models import Business, BusinessImage , Category

BUSINESS_CATEGORIES = [
    ('retail', 'Retail'),
    ('food', 'Food & Beverage'),
    ('tech', 'Technology'),
    ('health', 'Health & Wellness'),
    ('education', 'Education'),
    # Add more categories as needed
]


class BusinessProfileForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=True)
    operation_hours_opening = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    operation_hours_closing = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    
    class Meta:
        model = Business
        fields = ['name', 'category', 'description', 'location', 'address', 'phone']
        
    def save(self, commit=True):
        business = super().save(commit=False)
        business.operating_hours = {
            'opening': self.cleaned_data['operation_hours_opening'].strftime('%H:%M'),
            'closing': self.cleaned_data['operation_hours_closing'].strftime('%H:%M')
        }
        if commit:
            business.save()
        return business

class BusinessImageForm(forms.ModelForm):
    class Meta:
        model = BusinessImage
        fields = ['image', 'is_primary']