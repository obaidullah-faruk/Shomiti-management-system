from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import views

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('password/update/', views.PasswordChangeView.as_view(), name='password-change'),
    path('create/', views.MemberCreateView.as_view(), name='member-create'),
    path('members/', views.MemberList.as_view(), name='member-list'),
]
