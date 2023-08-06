from django.urls import path

from .views import RegisterView, LoginView, ProfileView, ProfileUpdateView, LogoutView

app_name = 'users'

urlpatterns = [
    path('users/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/update/', ProfileUpdateView.as_view(), name='profile_update'),
]