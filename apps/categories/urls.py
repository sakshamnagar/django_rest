from django.urls import path

from apps.categories.views.views import CategoryListAPIView, CategoryCreateAPIView, CategoryUpdateAPIView, CategoryDetailAPIView, CategoryDeleteAPIView, Bin, Restore

urlpatterns = [
    path('list', CategoryListAPIView.as_view(), name = 'list-category'),
    path('create', CategoryCreateAPIView.as_view(), name = 'create-category'),
    path('update/<int:pk>', CategoryUpdateAPIView.as_view(), name = 'update-category'),
    path('detail/<int:pk>', CategoryDetailAPIView.as_view(), name = 'detail-category'),
    path('delete/<int:pk>', CategoryDeleteAPIView.as_view(), name = 'delete-category'),
    path('bin/', Bin.as_view(), name = 'bin-category'),
    path('restore/<int:pk>', Restore.as_view(), name = 'restore-category'),

]
