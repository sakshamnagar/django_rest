from apps.products.serializers.serializers import ProductSerializer, ProductCreateSerializer
from apps.products.models import Product
from apps.products.filters.filters import ProductFilter

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveAPIView,DestroyAPIView,UpdateAPIView
from rest_framework.permissions import IsAuthenticated

from django.http import HttpResponse

from datetime import date, datetime



class ProductListAPIView(ListAPIView):
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter]
    filterset_class = ProductFilter
    ordering_fields = ['name']
    ##changing the default queryset method to return Products associated with the logged in vendor
    def get_queryset(self):
        if self.request.user.is_authenticated:
            vendor = self.request.user.vendor
            return Product.objects.filter(vendor=vendor).values_list('name','vendor','category')
        else:
            return Product.objects.values_list('name','vendor','category')
        

class ProductCreateAPIView(CreateAPIView):
    serializer_class = ProductCreateSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated]
    ##changing default create method to automatically assign vendor field as per logged in vendor before saving.
    def perform_create(self, serializer):
        serializer.save(vendor=self.request.user.vendor)


class ProductUpdateAPIView(UpdateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.filter(deleted_at__isnull = True)
    permission_classes = [IsAuthenticated]


class ProductDetailAPIView(RetrieveAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.filter(deleted_at__isnull = True)
    permission_classes = [IsAuthenticated]


class ProductDeleteAPIView(DestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.filter(deleted_at__isnull = True)
    permission_classes = [IsAuthenticated]
    #changing default delete method to soft delete items
    def perform_destroy(self, instance):
        instance.deleted_at = datetime.now()
        instance.save()

        
#method to list soft deleted items
class Bin(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,format=None):
        products = Product.all_objects.filter(deleted_at__isnull = False)
        serializer = ProductSerializer(products,many=True)
        return Response(serializer.data)
    
    
#method to restore soft deleted item
class Restore(APIView):    
    def post(request,pk):
        Product.all_objects.filter(pk=pk).update(deleted_at = None)
        return HttpResponse("Success")