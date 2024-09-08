from django.shortcuts import render
from rest_framework import viewsets
from .models import Brand, Product, ProductImage, Supplier, Supply
from .serializers import BrandSerializer, ProductSerializer, ProductImageSerializer, SupplierSerializer, SupplySerializer



def home(request):
    return render(request, 'store/home.html')  # Asegúrate de tener el archivo home.html en la carpeta templates


def index(request):
    return render(request, 'index.html')



class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductImageViewSet(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

class SupplyViewSet(viewsets.ModelViewSet):
    queryset = Supply.objects.all()
    serializer_class = SupplySerializer
