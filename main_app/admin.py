from django.contrib import admin
from .models import UserProfile, Apartment

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Apartment)