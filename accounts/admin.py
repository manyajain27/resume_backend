from django.contrib import admin
from .models import UserAccount

class UserAccountAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_active', 'is_staff', 'created_at', 'updated_at')  
    readonly_fields = ('created_at', 'updated_at')

admin.site.register(UserAccount, UserAccountAdmin)
