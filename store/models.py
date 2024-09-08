



from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
from image_cropping import ImageRatioField


class Brand(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name



class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
   
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='products')  # Marca por defecto



    # Otros campos relevantes para tu producto

    def __str__(self):
        return self.name
    
class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/images/')
    cropping = ImageRatioField('image', '430x360')  # Relación de aspecto para el recorte
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def save(self, *args, **kwargs):
        # Redimensionar la imagen
        img = Image.open(self.image)
    
        # Definir tamaño máximo
        max_size = (430, 360)
        img.thumbnail(max_size)

        # Guardar la imagen redimensionada
        img_io = BytesIO()
        img.save(img_io, format=img.format)
        img_io.seek(0)

        self.image = ContentFile(img_io.read(), name=self.image.name)

        super(ProductImage, self).save(*args, **kwargs)

    def clean(self):
        if self.product.images.count() >= 4:
            raise ValidationError("No se pueden agregar más de cuatro imágenes por producto.")

    def __str__(self):
        return f"Image for {self.product.name}"
    

class Supplier(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.name

class Supply(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    stock_min = models.PositiveIntegerField(default=10)

    class Meta:
        unique_together = ('supplier', 'product')

    def __str__(self):
        return f"{self.supplier.name} supplies {self.product.name}"
    
    def save(self, *args, **kwargs):
        if self.pk is None:
            # Check if Product has been saved before saving Supply
            if not self.product.pk:
                return  # Avoid saving if Product doesn't have a primary key
        super().save(*args, **kwargs)
        if self.verificar_stock():
            self.enviar_alerta_stock_bajo()
            
    def verificar_stock(self):
        return self.quantity < self.stock_min
    
    def enviar_alerta_stock_bajo(self):
        # Ejemplo de notificación: puedes modificarlo para enviar un correo electrónico, notificación, etc.
        print(f"Alerta: El stock del producto '{self.product.name}' suministrado por '{self.supplier.name}' está por debajo del mínimo.")
        
        # Enviar un correo electrónico de alerta
        send_mail(
            'Alerta de Stock Bajo',
            f'El stock del producto {self.product.name} está por debajo del mínimo establecido.',
            settings.DEFAULT_FROM_EMAIL,
            ['admin@example.com'],  # Cambia a la dirección de correo deseada
            fail_silently=False,
        )




    






