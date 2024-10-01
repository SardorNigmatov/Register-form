from django.contrib import admin
from .models import Users

# Register your models here.

@admin.register(Users)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'user_surname', 'phone_number', 'email', 'company', 'gender')
    search_fields = ('user_name', 'user_surname', 'email')
    list_filter = ('gender', 'company')
    ordering = ('user_name',)
