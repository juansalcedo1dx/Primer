from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Supply

@receiver(post_save, sender=Supply)
def verificar_stock_minimo(sender, instance, **kwargs):
    if instance.verificar_stock():
        instance.enviar_alerta_stock_bajo()
