from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('pages.urls')), #REFERENCIA A TODOS LOS URLS DEL PROYECTO
    path('admin/', admin.site.urls), #POR DEFECTO
]
