from django.urls import path
from . import views

urlpatterns = [
    path('rooms', views.rooms, name='rooms'),
    path('create_room', views.create_room, name='create_room'),
    path('browse_topics', views.browse_topics, name='browse_topics'),
    path('recent_activity', views.recent_activity, name='recent_activity'),
    path('delete_room/<str:pk>/', views.delete_room, name='delete_room'),
]