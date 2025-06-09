from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

# Define app_name for namespacing if you have multiple apps and same URL names
# app_name = 'fixit_frw'

urlpatterns = [
    # Authentication views
    path('signup/', views.authView, name="signup"), # Changed from authView to be more descriptive
    path('accounts/login/', views.user_login_view, name='login'), # Added a new view for login page if needed or use Django's
    path('accounts/logout/', views.user_logout_view, name='logout'), # Added a new view for logout

    # Django's built-in auth URLs (password reset, etc.)
    path("accounts/", include("django.contrib.auth.urls")), # This provides login, logout, password_reset, etc.

    # REST framework auth (if you are building an API)
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # Main application views
    path('', views.landing_page_view, name='landing_page'), # Assuming landing page is the root
    path('menu/', views.menu_page_view, name='menu_page'),
    path('menu/product_details', views.repairrequest_detail, name='product_details'),
    path('menu/product_details/chatpage/<int:item_id>/', views.chat_page_views, name='chatpage'),
    path('menu/product_details/fixit_success_page', views.fixit_success_view, name='fixit_success_page'),
    path('upload/', views.upload_item_view, name='upload_item'), # Renamed from uploadpage
    path('upload/success/', views.upload_success_view, name='upload_success'), # For the success page

    # Example for confirmation and map pages if managed by Django
    path('confirmation/<int:item_id>/', views.confirmation_page_view, name='confirmation_page'),
    path('maps_display/', views.maps_page_view, name='maps_page'),
    path('history/', views.history_page_view, name='history_page'),

    #testing
    path('repairlist/', views.repairrequest_list, name='repairrequest_list'),
    path('repair/<int:pk>/', views.repairrequest_detail, name='repairrequest_detail'),
]

# Apply format suffixes for API views if needed, usually for DRF viewsets or APIViews
# urlpatterns = format_suffix_patterns(urlpatterns)
