from apps.categories.models import Category
from apps.categories.serializers.serializers import CategorySerializers

from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework import filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser

from django.http import HttpResponse

from datetime import datetime



class CategoryListAPIView(ListAPIView):
    serializer_class = CategorySerializers
    queryset = Category.objects.all()
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name']


class CategoryCreateAPIView(CreateAPIView):
    serializer_class = CategorySerializers
    queryset = Category.objects.all()
    permission_classes = [IsAdminUser]


class CategoryUpdateAPIView(UpdateAPIView):
    serializer_class = CategorySerializers
    queryset = Category.objects.all()
    permission_classes = [IsAdminUser]


class CategoryDetailAPIView(RetrieveAPIView):
    serializer_class = CategorySerializers
    queryset = Category.objects.all()
    permission_classes = [IsAdminUser]
    

class CategoryDeleteAPIView(DestroyAPIView):
    serializer_class = CategorySerializers
    queryset = Category.objects.all()
    permission_classes = [IsAdminUser]
    def perform_destroy(self, instance):
        instance.deleted_at = datetime.now()
        instance.save()


class Bin(APIView):
    permission_classes = [IsAdminUser]
    def get(self,request,format=None):
        category = Category.all_objects.filter(deleted_at__isnull = False)
        serializer = CategorySerializers(category,many=True)
        return Response(serializer.data)

class Restore(APIView):
    def post(self,request,pk):
        Category.all_objects.filter(pk=pk).update(deleted_at = None)
        return HttpResponse("Success")