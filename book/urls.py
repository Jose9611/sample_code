from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import login,register_user,BookListAPIView,ApartmentAPIView,FlatAPIView,UserPermissionAPIView
from django.urls import path, re_path
urlpatterns = [
    # Obtain JWT token
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    # Refresh JWT token
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/', login, name='login'),
    path('add-permission',UserPermissionAPIView.as_view(),name='add-permission'),
    path('staff-register/',register_user,name='register'),
    path('book-list/', BookListAPIView.as_view(), name='book_list'),
    path('apartment/', ApartmentAPIView.as_view(), name='apartment'),
    path('add-flat/', FlatAPIView.as_view(), name='add-flat'),

]
