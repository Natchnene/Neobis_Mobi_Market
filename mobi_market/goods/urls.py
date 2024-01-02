from django.urls import path, include
from rest_framework import routers

from .views import (
    CardProductLongCreateAPIView,
    CardProductShortAllListAPIView,
    CardProductShortUserListAPIView,
    CardProductShortLikedListAPIView,
    CarsProductLikeGenericAPIView,
)

router = routers.DefaultRouter()
router.register('product', CardProductLongCreateAPIView, basename='my_products')

urlpatterns = [
    path("", include(router.urls)),
    path('products_all/', CardProductShortAllListAPIView.as_view(), name='products_all_main_page'),
    path('products_user/', CardProductShortUserListAPIView.as_view(), name='products_user'),
    path('products_user_liked/', CardProductShortLikedListAPIView.as_view(), name='products_user_liked'),
    path('product/like/<int:id>/', CardProductShortLikedListAPIView.as_view(), name='product_like'),
]

