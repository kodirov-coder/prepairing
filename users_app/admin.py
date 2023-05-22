from django.contrib import admin
from .models import Users, EmailVerification

from products_app.admin import BasketAdmin


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('username', "last_name")
    inlines = (BasketAdmin,)

@admin.register(EmailVerification)
class EmailVerificationAdmin(admin.ModelAdmin):
    list_display = ("code", "user", "expiration")
    fields = ("code", "user", "created_at", "expiration")
    readonly_fields = ("created_at", "user")