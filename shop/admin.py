from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Category, Shop, Item


@admin. register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['icon_img', 'name', 'is_public']
    list_display_links = ['name']
    list_filter = ['is_public']
    search_fields = ['name']

    def icon_img(self, category):
        if category.icon:
            img_tag = '<img src="{}" style="max-width: 72px;" />'
            return mark_safe(img_tag.format(category.icon.url))
        return None


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    pass


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    pass


