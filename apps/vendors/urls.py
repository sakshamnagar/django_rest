from django.urls import path
from apps.vendors.views.views import VendorListAPIView, VendorCreateAPIView, VendorUpdateAIPView, VendorDetailAPIView, VendorDeleteAPIView, Bin, Restore

urlpatterns = [
    path('list', VendorListAPIView.as_view(), name = 'list-vendor'),
    path('create', VendorCreateAPIView.as_view(), name = 'create-vendor'),
    path('update/<int:pk>', VendorUpdateAIPView.as_view(), name = 'update-vendor'),
    path('detail/<int:pk>', VendorDetailAPIView.as_view(), name = 'detail-vendor'),
    path('delete/<int:pk>', VendorDeleteAPIView.as_view(), name = 'delete-vendor'),
    path('bin/', Bin.as_view(), name = 'bin-vendor'),
    path('restore/<int:pk>', Restore.as_view(), name = 'restore-vendor'),

]
