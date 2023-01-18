from django.contrib import admin

from generator.models import GenPass


class GenPassAdmin(admin.ModelAdmin):
    list_display = ('user', 'site', 'time')
    list_filter = ('user', 'site', 'time')
    search_fields = ('user',)


# Register your models here.
admin.site.register(GenPass, GenPassAdmin)
# Register genpass model
