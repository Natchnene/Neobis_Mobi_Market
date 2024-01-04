from django.urls import path, include
from rest_framework import routers

from .views import (
    CardProductLongCreateAPIView,
    CardProductShortAllListAPIView,
    CardProductShortUserListAPIView,
    CardProductShortLikedListAPIView,
    CardProductLikeGenericAPIView,
    CardProductUnLikeGenericAPIView
)

router = routers.DefaultRouter()
router.register('product', CardProductLongCreateAPIView, basename='my_products')

urlpatterns = [
    path("", include(router.urls)),
    path('products_all/', CardProductShortAllListAPIView.as_view(), name='products_all_main_page'),
    path('products_user/', CardProductShortUserListAPIView.as_view(), name='products_user'),
    path('products_user_liked/', CardProductShortLikedListAPIView.as_view(), name='products_user_liked'),
    path('product/<int:product_id>/like/', CardProductLikeGenericAPIView.as_view(), name='product_like'),
    path('product/<int:product_id>/unlike/', CardProductUnLikeGenericAPIView.as_view(), name='product_unlike'),
]

