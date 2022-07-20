from django.contrib import admin
from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('name','email','is_staff','is_superuser','is_active')

admin.site.register(UserProfile, UserProfileAdmin)