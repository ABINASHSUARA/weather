# app/urls.py
from django.urls import path
from .views import home, registration, user_login, user_logout, search, user_history, all_history

urlpatterns = [
    path('', home, name='home'),  # Home page view
    path('registration/', registration, name='registration'),  # Registration page
    path('user_login/', user_login, name='user_login'),  # Login page
    path('user_logout/', user_logout, name='user_logout'),  # Logout page
    path('search/', search, name='search'),  # Search page
    path('user_history/', user_history, name='user_history'),  # User-specific history
    path('all_history/', all_history, name='all_history'),  # All history page
]
