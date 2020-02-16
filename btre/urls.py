from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('pages.urls')), #Referencia a los urls de la app pages
    path('listings/', include('listings.urls')), #Referencia a los urls de la app listings
    path('admin/', admin.site.urls), #POR DEFECTO
]
