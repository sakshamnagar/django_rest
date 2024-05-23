from apps.users.views.views import index, UserCreateAPIView, UserListView, UserUpdateAPIView, UserLoginView, LogoutView

from django.urls import path



urlpatterns = [
    path('', index, name = 'index'),
    path('signup', UserCreateAPIView.as_view(), name = 'signup'),
    path('users', UserListView.as_view(), name = 'users'),
    path('users/update/<int:pk>', UserUpdateAPIView.as_view(), name = 'update-user'),
    path('login', UserLoginView.as_view(), name = 'login'),
    path('logout', LogoutView.as_view(), name = 'logout'),
]
