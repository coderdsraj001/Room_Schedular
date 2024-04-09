from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name="home"),
    path('rooms/', views.index, name="index"),
    path('rooms/create-room/', views.create_room, name="create_room"), 
    path('rooms/edit-room/<int:id>', views.edit_class, name="edit_class"), 
    path('rooms/delete_room/<int:id>', views.delete_room, name="delete_room"), 
    path('rooms/<int:room_id>/book/', views.make_booking, name='make_booking'),
    path("register/", views.register_request, name="register"),
    path("login/", views.login_request, name="login"),
    path("logout/", views.logout_request, name= "logout"),

]