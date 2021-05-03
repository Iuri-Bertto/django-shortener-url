from rest_framework import serializers

from ..models import OfflineUrl


class OfflineUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfflineUrl
        fields = '__all__'

    def create(self, validated_data):
        # Searching if already exists some URL with the passed value avoiding increase shortened URL's
        url = OfflineUrl.objects.filter(original_url=validated_data["original_url"]).filter(
            result__isnull=False).first()
        if url:
            return url

        return OfflineUrl.objects.create(**validated_data)
