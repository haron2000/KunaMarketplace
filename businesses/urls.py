from django.urls import path
from . import views
from businesses import views

app_name = 'businesses'

urlpatterns = [
    # We'll add URLs here once we create the views
    # For now, let's just add a placeholder view
    path('create-profile/', views.create_business_profile, name='create_business_profile'),
    path('create/', views.create_business_profile, name='create_business_profile'),
    path('', views.business_list, name='business_list'),
    path('profile/', views.business_profile, name='business_profile'),
    path('profile/edit/', views.edit_business_profile, name='edit_profile'),
    path('<int:business_id>/', views.business_detail, name='detail'),
    path('list/', views.business_list, name='list'),
]