from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BrandViewSet, ProductViewSet, ProductImageViewSet, SupplierViewSet, SupplyViewSet

router = DefaultRouter()
router.register(r'brands', BrandViewSet)
router.register(r'products', ProductViewSet)
router.register(r'product-images', ProductImageViewSet)
router.register(r'suppliers', SupplierViewSet)
router.register(r'supplies', SupplyViewSet)

urlpatterns = [
    path('', include(router.urls)),
]


