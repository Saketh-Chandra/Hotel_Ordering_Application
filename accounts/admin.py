from django.contrib import admin
from .models import CustomUser
from .form import CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin


# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm

    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Info',
            {
                'fields': (
                    'DOB',
                    'phone_number',
                    'Gender',
                    'address1',
                    'address2',
                    'zip_code',
                    'city',
                    'country'
                )
            }
        )
    )


admin.site.register(CustomUser, CustomUserAdmin)
