from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('create-technique', views.createTechnique, name='create-technqiue'),
    path('technique/<str:pk>', views.techniqueView, name='technique'),
    path('update-technique/<str:pk>', views.updateTechnique, name='update-technique'),
    path('delete-technique/<str:pk>', views.deleteTechnique, name='delete-technique'),

    path('position/<str:name>', views.positionView, name='position'),

    
]
