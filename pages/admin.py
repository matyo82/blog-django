from django.contrib import admin
from .models import Service, Team

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'summary')
    search_fields = ('title', 'summary')

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('full_name',)
