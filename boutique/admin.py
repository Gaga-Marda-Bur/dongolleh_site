from django.contrib import admin
from .models import BackgroundImage, Bague
from adminsortable2.admin import SortableAdminMixin  # only needed for admin
from django.utils.html import format_html

@admin.register(BackgroundImage)
class BackgroundImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('thumbnail', 'title', 'active')
    list_filter = ('active',)

    def thumbnail(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" style="border-radius: 8px;" />', obj.image.url)
        return "No Image"

    thumbnail.short_description = "Preview"


@admin.register(Bague)
class BagueAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prix')
