from rest_framework import serializers
from .models import Brand, Product, ProductImage, Supplier, Supply

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'

class SupplySerializer(serializers.ModelSerializer):
    supplier = SupplierSerializer(read_only=True)
    product = ProductSerializer(read_only=True)

    class Meta:
        model = Supply
        fields = '__all__'
