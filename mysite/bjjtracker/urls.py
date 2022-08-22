from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),

    path('', views.home, name='home'),

    path('create-technique/', views.createTechnique, name='create-technique'),
    path('technique/<str:pk>/', views.techniqueView, name='technique'),
    path('update-technique/<str:pk>/', views.updateTechnique, name='update-technique'),
    path('delete-technique/<str:pk>/', views.deleteTechnique, name='delete-technique'),

    path('position/<str:name>/', views.positionView, name='position'),

    path('move-of-the-day/', views.moveOfTheDay, name='move-of-the-day'),
    path('move-of-the-day-history/', views.moveOfTheDayHistory, name='move-of-the-day-history'),
]
