from rest_framework import viewsets

from ..serializers.TinyUrlSerializer import TinyUrlSerializer
from ..models import TinyUrl


class TinyUrlViewSet(viewsets.ModelViewSet):
    serializer_class = TinyUrlSerializer
    queryset = TinyUrl.objects.all()
    ordering_fields = '__all__'
    search_fields = {'id', 'original_url', 'result'}
