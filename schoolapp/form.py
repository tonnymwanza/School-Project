from django import forms
from .models import Profile, Question
from django.contrib.auth.models import User

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
           "email",
           "first_name",
           "last_name",
           "username"
        )


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = [
            "question", 
            "answer_one",
            "answer_two",
            "answer_three",
            "answer_four"
        ]