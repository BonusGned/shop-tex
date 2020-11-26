from django.urls import path
from .api_views import (
    CategoryListApiView,
    SmartphoneListAPIView,
    NotebookListAPIView,
    SmartphoneDetailAPIView,
    NotebookDetailAPIView,
    CustomerListAPIView
)


urlpatterns = [
    path('categories/', CategoryListApiView.as_view(), name='categories_list'),
    path('customers/', CustomerListAPIView.as_view(), name='customers_list'),
    path('smartphones/', SmartphoneListAPIView.as_view(), name='smartphones_list'),
    path('notebooks/', NotebookListAPIView.as_view(), name='notebooks_list'),
    path('smartphones/<str:id>', SmartphoneDetailAPIView.as_view(), name='smartphone_detail'),
    path('notebooks/<str:id>', NotebookDetailAPIView.as_view(), name='notebook_detail'),
]