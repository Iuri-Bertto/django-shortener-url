from django.contrib import admin
from .models import TinyUrl, OfflineUrl

admin.site.register(TinyUrl)
admin.site.register(OfflineUrl)
