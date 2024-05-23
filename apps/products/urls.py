from apps.products.views.views import ProductListAPIView, ProductCreateAPIView, ProductUpdateAPIView, ProductDetailAPIView, ProductDeleteAPIView, Bin, Restore

from django.urls import path



urlpatterns = [
    path('list', ProductListAPIView.as_view(), name = 'list-product'),
    path('create', ProductCreateAPIView.as_view(), name = 'create-product'),
    path('update/<int:pk>', ProductUpdateAPIView.as_view(), name = 'update-product'),
    path('detail/<int:pk>', ProductDetailAPIView.as_view(), name = 'detail-product'),
    path('delete/<int:pk>', ProductDeleteAPIView.as_view(), name = 'delete-product'),
    path('bin', Bin.as_view(), name = 'bin-product'),
    path('restore/<int:pk>', Restore.as_view(), name = 'restore-product'),
]
