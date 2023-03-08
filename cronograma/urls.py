from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='cronograma'),
    path('view_crono/<int:id>', views.view_crono, name='view_crono'),
    path('create_crono/', views.create_crono, name='create_crono'),
    path('delete/<int:misa>', views.delete, name='misa_delete'),
    path('musico', views.create_musico, name='create_musico'),
]