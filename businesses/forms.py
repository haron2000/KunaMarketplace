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
    
    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('operation_hours_opening') and cleaned_data.get('operation_hours_closing'):
            opening_time = cleaned_data['operation_hours_opening']
            closing_time = cleaned_data['operation_hours_closing']
            if opening_time >= closing_time:
                raise forms.ValidationError("Closing time must be after opening time.")
        
        
    
        if hasattr(self.instance, 'owner') and Business.objects.filter(owner=self.instance.owner).exists():
            raise forms.ValidationError("You already have a business profile.")
        return cleaned_data
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