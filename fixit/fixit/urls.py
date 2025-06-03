"""
URL configuration for fixit project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# from fixit_frw import views # Removed direct import of app views here

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('fixit_frw.urls')), # Include app-specific URLs
    # The following lines are now handled within fixit_frw.urls or are redundant
    # path('menu/', views.menu_page, name='MenuPage'),
    # path('menu/upload', views.upload_page, name='uploadPage'),
]

# Serve static and media files during development only
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)