from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    PROFILE_TYPE_CHOICES = [
        ('personal', 'Personal'),
        ('business', 'Business'),
    ]
    profile_type = models.CharField(
        max_length=10,
        choices=PROFILE_TYPE_CHOICES,
        default='personal'
    )
    # Additional fields for customization if needed
    # e.g., phone number, profile image, etc.

class BusinessProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='business_profile')
    business_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    photos = models.ImageField(upload_to='business_photos/', blank=True, null=True)

    def __str__(self):
        return self.business_name
