from django.db import models
from django.utils import timezone
import random


import datetime, string


class Url(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    original_url = models.TextField()
    result = models.CharField(max_length=255, null=True, blank=True)
    expiration_date = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['-created']

    @property
    def is_expired(self):
        today = timezone.now().date()
        if self.expiration_date < today:
            self.delete()
            return True

        return False

    def save(self, *args, **kwargs):
        super(Url, self).save(*args, **kwargs)

        if self.expiration_date is None:
            self.expiration_date = (timezone.now() + datetime.timedelta(days=7)).date()
            self.save()

    def __str__(self):
        return self.original_url


class TinyUrl(Url):
    class Meta:
        ordering = ['-created']


class OfflineUrl(Url):
    API_ENDPOINT = "http://127.0.0.1:8000"
    MODULE_ENDPOINT = "/api/u/"

    opcional_path = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        ordering = ['-created']

    def save(self, *args, **kwargs):
        super(OfflineUrl, self).save(*args, **kwargs)

        if self.result is not None:
            return

        # Verifying if some URL exists with the provided opcional_path
        short_url = None
        if self.opcional_path:
            short_url = self.API_ENDPOINT + self.MODULE_ENDPOINT + self.opcional_path

        # Making the URL based on the existence of the URL or not
        url_exists = Url.objects.filter(result=short_url).first()
        if not url_exists:
            self.result = short_url
        else:
            self.result = self.API_ENDPOINT + self.MODULE_ENDPOINT + ''.join(
                random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(5))

        self.save()
