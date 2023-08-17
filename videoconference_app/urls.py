from django.urls import path
from . import views
#use to generate pattern for when a view is created this will the path with the help they will render the file
urlpatterns = [
    path('register/',views.register, name = 'register'),
    path('login/',views.login_view, name = 'login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('meeting/', views.videocall, name='meeting'),
    path('logout/', views.logout_view, name='logout'),
    path('join/', views.join_room, name='join_room'),
]