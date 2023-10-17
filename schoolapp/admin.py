from django.contrib import admin
from .models import Question
from .models import Profile
# Register your models here.

@admin.register(Question)
class AdminQuiz(admin.ModelAdmin):
    list_display = (
        "question", "answer_one", "answer_two", "answer_three", "answer_four"
    )

@admin.register(Profile)
class AdminProfile(admin.ModelAdmin):
    list_display = [
        "user"
    ]
