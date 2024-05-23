from apps.vendors.models import Vendor
from apps.vendors.serializers.serializers import VendorSerializers
from apps.users.models import User, Role

from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework import filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import DjangoModelPermissions, IsAuthenticated

from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from datetime import datetime


"""def list(request):
    if request.method == "GET":
        vendors = Vendor.objects.all()
        serializer = VendorSerializers(vendors, many=True)
        return Response(serializer.data, safe=False)

        
@api_view(['GET', 'POST'])
def add(request):
    if request.method == 'POST':
        serializer = VendorSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)"""

"""class VendorList(APIView):
    def get(self,request,format=None):
        vendors = Vendor.objects.all()
        serializer = VendorSerializers(vendors,many=True)
        return Response(serializer.data)
    
    def post(self,request,format=None):
        serializer = VendorSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
"""    

"""class VendorDetail(APIView):
    def get_object(self,pk):
        try:
            return Vendor.objects.get(pk=pk)
        except Vendors.DoesNotExist:
            raise Http404
        
    def get(self,request,pk):
        vendor = self.get_object(pk)
        serializer = VendorSerializers(vendor)
        return Response(serializer.data)
    def patch(self,request,pk):
        vendor = self.get_object(pk)
        # For patch use partial=true in order to send data only for fields which you want to update instead of all fields. 
        # For PUT you will need to enter data for all fields.
        
        serializer = VendorSerializers(vendor,request.data,partial=True)
        if serializer.is_valid():                                         
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        vendor = self.get_object(pk)
        vendor.soft_del()
        return Response(status=status.HTTP_204_NO_CONTENT)   
"""    

"""lass VendorDetail(LoginRequiredMixin,generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializers
"""



class VendorListAPIView(ListAPIView):
    serializer_class = VendorSerializers
    queryset = Vendor.objects.only('id', 'user', 'image').select_related('user')
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    search_fields = ['first_name', 'last_name']
    ordering_fields = ['pk', 'first_name']


class VendorCreateAPIView(CreateAPIView):
    serializer_class = VendorSerializers
    permission_classes = [IsAuthenticated]
    queryset = Vendor.objects.all()
    def perform_create(self, serializer):
        role = Role.objects.get(name="Vendor")
        User.objects.filter(id=self.request.user.id).update(role=role.id)
        serializer.save(user=self.request.user)


class VendorUpdateAIPView(UpdateAPIView):
    serializer_class = VendorSerializers
    queryset = Vendor.objects.only('id', 'user', 'image').select_related('user')
    permission_classes = [DjangoModelPermissions]


class VendorDeleteAPIView(DestroyAPIView):
    serializer_class = VendorSerializers
    queryset = Vendor.objects.only('id', 'user', 'image').select_related('user')
    permission_classes = [DjangoModelPermissions]
    #changing default delete method to soft delete vendors
    def perform_destroy(self, instance):
        instance.deleted_at = datetime.now()
        instance.save()


class VendorDetailAPIView(RetrieveAPIView):
    serializer_class = VendorSerializers
    queryset = Vendor.objects.only('id', 'user', 'image').select_related('user')
    permission_classes = [DjangoModelPermissions]


#method to list soft deleted items
class Bin(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,format=None):
        vendors = Vendor.all_objects.filter(deleted_at__isnull = False)
        serializer = VendorSerializers(vendors,many=True)
        return Response(serializer.data)


#method to restore softdeleted items
class Restore(APIView): 
    def post(request,pk):
        Vendor.all_objects.filter(pk=pk).update(deleted_at = None)
        return HttpResponse("Success")


