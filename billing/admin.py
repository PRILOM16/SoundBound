from django.contrib import admin
from .models import Purchase

@admin.register(Purchase)
class PurсhaseAdmin(admin.ModelAdmin):
    list_display = ('user', 'song', 'purchase_date')

    list_filter = ('purchase_date', 'user')

    search_fields = ('user__username', 'song__title')