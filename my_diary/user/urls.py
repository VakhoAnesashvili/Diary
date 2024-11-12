from django.urls import path
from .views import RegisterView, LoginView, LogoutView, UserProfileRetrieveView, UserProfileUpdateView, UserProfileDeleteView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    
    path('profile/', UserProfileRetrieveView.as_view(), name='profile-retrieve'),  
    path('profile/update/', UserProfileUpdateView.as_view(), name='profile-update'),  
    path('profile/delete/', UserProfileDeleteView.as_view(), name='profile-delete'),  
]
