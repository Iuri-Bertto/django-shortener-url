from rest_framework import viewsets

from ..serializers.OfflineUrlSerializer import OfflineUrlSerializer
from ..models import OfflineUrl


class OfflineUrlViewSet(viewsets.ModelViewSet):
    serializer_class = OfflineUrlSerializer
    queryset = OfflineUrl.objects.all()
    ordering_fields = '__all__'
    search_fields = {'id', 'original_url', 'result'}
