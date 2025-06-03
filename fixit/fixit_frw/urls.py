from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.authView, name="authView"),  # Root page: login/signup
    path('signup/', views.authView, name="signup"),  # Optional separate signup route
    path('accounts/', include("django.contrib.auth.urls")),  # Login/logout/password views
    path('api-auth/', include('rest_framework.urls')),  # DRF login
    path('menu/', views.menu_page, name='Menupage'),
    path('menu/upload', views.upload_page, name='uploadpage'),
]
urlpatterns = format_suffix_patterns(urlpatterns)
