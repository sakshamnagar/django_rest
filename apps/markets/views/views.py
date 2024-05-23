from rest_framework.views import APIView
from rest_framework import filters
from rest_framework.generics import CreateAPIView,ListAPIView,UpdateAPIView,RetrieveAPIView,DestroyAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser

from apps.markets.models import Market
from apps.markets.serializers.serializers import MarketSerializer
from apps.vendors.models import Vendor

from django.http import HttpResponse

from datetime import datetime



class MarketListAPIView(ListAPIView):
    serializer_class = MarketSerializer
    queryset = Market.objects.prefetch_related('vendors')
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name']


class MarketCreateAPIView(CreateAPIView):
    serializer_class = MarketSerializer
    queryset = Market.objects.all()
    permission_classes = [IsAdminUser]


class MarketUpdateAIPView(UpdateAPIView):
    serializer_class = MarketSerializer
    queryset = Market.objects.all()
    permission_classes = [IsAdminUser]


class MarketDeleteAPIView(DestroyAPIView):
    serializer_class = MarketSerializer
    queryset = Market.objects.all()
    permission_classes = [IsAdminUser]
    def perform_destroy(self, instance):
        instance.deleted_at = datetime.now()
        instance.save()


class MarketDetailAPIView(RetrieveAPIView):
    serializer_class = MarketSerializer
    queryset = Market.objects.all()
    permission_classes = [IsAdminUser]


class Bin(APIView):
    permission_classes = [IsAdminUser]
    def get(self,request,format=None):
        market = Market.all_objects.filter(deleted_at__isnull=False)
        serializer = MarketSerializer(market,many=True)
        return Response(serializer.data)
    

class Restore(APIView):    
    def post(self,request,pk):
        Market.all_objects.filter(pk=pk).update(deleted_at = None)
        return HttpResponse("Success")
