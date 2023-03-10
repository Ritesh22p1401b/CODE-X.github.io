from os import name
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginpage, name="login"),
    path('register/', views.registerpage, name="register"),
    path('logout/', views.logoutuser, name="logout"),
    path('',views.home, name="home"),
    path('room/<str:pk>/',views.room,name="room" ),
    path('profile/<str:pk>',views.userProfile,name="user-profile"),
    path('create-room/', views.createRoom, name="create-room"),
    path('update-room/<str:pk>/', views.updateRoom, name="update-room"),   
    path('delete-room/<str:pk>/', views.deleteRoom, name="delete-room"),
    path('delete-message/<str:pk>/', views.deleteMessage, name="delete-message"),
    path("contact/",views.contact_us,name="contact"),
    path("course/",views.courses,name="course")
]
