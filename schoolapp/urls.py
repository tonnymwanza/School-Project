from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('home', views.home, name="home"),
    path('', views.index, name="index"),
    path('adminstrator', views.adminstrator, name="adminstrator"),
    path('teachers', views.teachers, name="teachers"),
    path('students', views.students, name="students"),
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('about', views.about, name="about"),
    path('success', views.success, name="success"),
    path('password_change', views.password_change, name="password_change"),
    path('student_profile', views.student_profile, name="student_profile"),
    path('logout', views.logout, name="logout"),
    path('correct_choice', views.correct_choice, name="correct_choice"),
    path('password_reset', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_complete', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('edit',views.edit, name="edit"),
]