"""imports"""
from django.apps import AppConfig

class CheckoutConfig(AppConfig):
    """check config """
    name = 'checkout'

    def ready(self):
        import checkout.signals
