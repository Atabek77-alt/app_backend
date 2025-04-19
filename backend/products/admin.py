from django.contrib import admin
from .models import *

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'bio']


@admin.register(Product)
class  ProductAdmin(admin.ModelAdmin):
    list_display = ['owner', 'title']
    filter_horizontal = ('tags',)

    def display_tags(self, obj):
        return ", ".join([tag.name for tag in obj.tags.all()])

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
