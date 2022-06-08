from django.contrib import admin

from backend.apps.accounts.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
