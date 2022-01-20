from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('CORE.urls')),
    path('About/', include('ABOUTUS.urls', namespace='ABOUTUS')),
    path('Accessory/', include('ACCESSORY.urls', namespace='ACCESSORY')),
    path('Backpack/', include('BACKPACK.urls' , namespace='BACKPACK')),
    path('Clothes/', include('CLOTHES.urls', namespace='CLOTHES')),
    path('News/', include('NEWS.urls', namespace='NEWS')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)