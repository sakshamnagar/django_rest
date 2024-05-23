from django.http import HttpResponse
from django.contrib.auth import logout

from rest_framework.generics import CreateAPIView,UpdateAPIView,ListAPIView
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from apps.users.serializers.serializers import UserSerializer, UserCreateSerializer, UserLoginSerializer
from apps.users.models import User



def index(request):
    return HttpResponse("Welcome!")


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.filter(deleted_at__isnull = True)


class UserListView(ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.filter(deleted_at__isnull = True)
    

class UserUpdateAPIView(UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.filter(deleted_at__isnull = True)


class UserLoginView(TokenObtainPairView):
    serializer_class = UserLoginSerializer


class LogoutView(APIView):
    def get(self, request):
        logout(request)
        return HttpResponse("Logged Out.")

