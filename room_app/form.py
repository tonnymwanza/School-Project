from django import forms
from . models import Room_details

class Room_detailsForm(forms.ModelForm):
    class Meta:
        model = Room_details
        fields = [
            "host",
            "room_name",
            "topic",
            "room_description",
        ]