from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from accounts.models import Account
# Register your models here.


class AccountAdmin(BaseUserAdmin):
    fieldsets = [
        ("Personal Info", {"fields": ["email", 'password', 'phone',
         'name']}),
        ("User Permission", {'fields': [
         'is_superuser', 'is_active', 'is_staff', "user_permissions", 'groups']})
    ]

    add_fieldsets = [
        ("Personal", {"fields": [
            "email",  'name', 'phone', "password1",
            "password2",
        ]})
    ]
    list_display = ["name", "email", "phone", 'is_superuser']
    ordering = ['name']


# admin.site.unregister(User)
admin.site.register(Account, AccountAdmin)
