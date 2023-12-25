from django.contrib import admin

from pages.models import ScrollModel, GaleryModel

# Register your models here.

@admin.register(ScrollModel)
class ScrollModelAdmin(admin.ModelAdmin):
    list_dsplay = ['id', 'title', 'discount', 'created_at']
    search_fields = ['title', 'description']
    list_filter = ['created_at', 'updadet_at']
    ordering = ['-created_at']


@admin.register(GaleryModel)
class ScrollModelAdmin(admin.ModelAdmin):
    list_dsplay = ['id', 'image', 'created_at']
    list_filter = ['created_at', 'updadet_at']
    ordering = ['-created_at']

    