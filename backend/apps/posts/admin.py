from django.contrib import admin

from .models import *

# Register your models here.

@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    list_display = [
        'description',
        'image',
        'is_active',
    ]

