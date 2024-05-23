from django.urls import path

from apps.markets.views.views import MarketListAPIView, MarketCreateAPIView, MarketUpdateAIPView, MarketDetailAPIView, MarketDeleteAPIView, Bin, Restore

urlpatterns = [
    path('list', MarketListAPIView.as_view(), name = 'list-market'),
    path('create', MarketCreateAPIView.as_view(), name = 'create-market'),
    path('update/<int:pk>', MarketUpdateAIPView.as_view(), name = 'update-market'),
    path('detail/<int:pk>', MarketDetailAPIView.as_view(), name = 'detail-market'),
    path('delete/<int:pk>', MarketDeleteAPIView.as_view(), name = 'delete-market'),
    path('bin/', Bin.as_view(), name = 'bin-market'),
    path('restore/<int:pk>', Restore.as_view(), name = 'restore-market'),

]
