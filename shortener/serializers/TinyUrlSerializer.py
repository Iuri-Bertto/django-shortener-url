from rest_framework import serializers

from ..models import TinyUrl


class TinyUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = TinyUrl
        fields = '__all__'
