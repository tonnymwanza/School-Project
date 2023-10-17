from django.contrib import admin
from . models import Room_details
# Register your models here.

@admin.register(Room_details)
class Room_detailsAdmin(admin.ModelAdmin):
    list_display = [
        "host",
        "room_name",
        "topic",
        "room_description",
        "created",
        "updated"
    ]