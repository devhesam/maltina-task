from django.contrib import admin
from products.models import Product, Rating


@admin.register(Product)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'code', 'price', 'is_active', 'created_time', 'updated_time']
    list_filter = ['is_active', 'created_time', 'updated_time']
    list_editable = ['is_active']
    readonly_fields = ['created_time', 'updated_time']
    search_fields = ['name']
