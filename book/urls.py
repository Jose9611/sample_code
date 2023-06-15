from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import login,register_user,BookListAPIView
from django.urls import path, re_path
urlpatterns = [
    # Obtain JWT token
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    # Refresh JWT token
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/', login, name='login'),
    path('register/',register_user,name='register'),
    path('book-list/', BookListAPIView.as_view(), name='book_list'),

]