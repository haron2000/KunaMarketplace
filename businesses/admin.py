from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Business, Category, BusinessImage

@admin.register(Business)
class BusinessAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'category', 'location', 'created_at')
    search_fields = ('name', 'location', 'category__name')
    list_filter = ('category', 'created_at')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(BusinessImage)
class BusinessImageAdmin(admin.ModelAdmin):
    list_display = ('business', 'image', 'is_primary', 'uploaded_at')
    list_filter = ('is_primary', 'uploaded_at')
