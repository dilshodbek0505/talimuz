from django.contrib import admin
from .models import (
    School, 
    SchoolImage,
)


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ("id","user", "name", "address" )


@admin.register(SchoolImage)
class SchoolImageAdmin(admin.ModelAdmin):
    list_display = ("id", "school")
