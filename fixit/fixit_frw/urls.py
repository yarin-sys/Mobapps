
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('signup/', views.authView, name="authView"),
    path("accounts/", include("django.contrib.auth.urls")),
    path('api-auth/', include('rest_framework.urls')),
    path('menu/', views.menu_page, name='menupage'),
    path('menu/upload', views.upload_page, name='uploadpage'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
