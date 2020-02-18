from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('pages.urls')), #Referencia a los urls de la app pages
    path('listings/', include('listings.urls')), #Referencia a los urls de la app listings
    path('admin/', admin.site.urls), #POR DEFECTO
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)

