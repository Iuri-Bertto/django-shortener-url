from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import TinyUrl

import pyshorteners


@receiver(post_save, sender=TinyUrl)
def decrease_url(sender, instance, created, *args, **kwargs):
    # Only if it's created
    if created:
        shortener = pyshorteners.Shortener()
        instance.result = shortener.tinyurl.short(instance.original_url)
        instance.save()
