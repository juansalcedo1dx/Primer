from django.apps import AppConfig


class StoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'store'


class StoreConfig(AppConfig):
    name = 'store'  # Replace 'your_app' with the actual app name

    def ready(self):
        # Import signals to connect them
        import store.signals