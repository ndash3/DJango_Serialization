from django.contrib import admin
from .models import PassengerClass

# Register your models here.
@admin.register(PassengerClass)
class PassengerAdmin(admin.ModelAdmin):
    list_display = ['name', 'city', 'rewards']

