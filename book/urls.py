from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import login,register_user,UserSearchAPIView,FriendRequestAPIView,AcceptedListAPIView

from django.urls import path, re_path
app_name = 'book'
urlpatterns = [
    # Obtain JWT token
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    # Refresh JWT token
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/', login, name='login'),
    path('register/', register_user, name='register'),
    path('search/',UserSearchAPIView.as_view(),name='search'),
    path('friend-request/', FriendRequestAPIView.as_view(), name='friend-request'),
    path('friend-acceptedList/', AcceptedListAPIView.as_view(), name='friend-acceptedList'),


]
