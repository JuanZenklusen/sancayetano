from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cronograma/', include('cronograma.urls')),
    path('', views.index, name='index'),
]
