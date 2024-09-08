from django.contrib import admin
from image_cropping import ImageCroppingMixin
from .models import Product, ProductImage, Supply, Supplier, Brand

# Definir ProductImageInline primero
class ProductImageInline(ImageCroppingMixin, admin.TabularInline):
    model = ProductImage
    extra = 1  # Número de formularios vacíos que se muestran
    max_num = 4  # Limita el número de imágenes a 4

# Registrar el modelo Product
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']  # Campos que se mostrarán en la lista del admin
    search_fields = ['name']  # Habilitar búsqueda por nombre de producto
    inlines = [ProductImageInline]  # Añadir imágenes en línea
    def save_model(self, request, obj, form, change):
        # Guarda el Product primero
        if not obj.pk:
            super().save_model(request, obj, form, change)
        # Luego guarda las imágenes relacionadas si hay alguna
        super().save_model(request, obj, form, change)


# Registrar el modelo ProductImage
@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['product']  # Mostrar el producto asociado
    search_fields = ['product__name']  # Habilitar búsqueda por nombre de producto asociado

# Registrar el modelo Supply
@admin.register(Supply)
class SupplyAdmin(admin.ModelAdmin):
    list_display = ['supplier', 'product', 'price', 'quantity']  # Campos que se mostrarán en la lista del admin
    search_fields = ['product__name', 'supplier__name']  # Habilitar búsqueda por nombre de producto y proveedor

# Registrar el modelo Supplier
@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ['name']  # Campos que se mostrarán en la lista del admin
    search_fields = ['name']  # Habilitar búsqueda por nombre de proveedor


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
