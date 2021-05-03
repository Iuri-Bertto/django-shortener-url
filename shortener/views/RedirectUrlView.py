from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.response import Response

from django.shortcuts import redirect

from ..models import OfflineUrl


class RedirectUrlView(APIView):
    # Everybody can hit my endpoint
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        api_path = OfflineUrl.API_ENDPOINT
        url_path = request.get_full_path()
        short_url = api_path + url_path

        # Checking if some URL exists with the shortened value provided
        short_url = OfflineUrl.objects.filter(result=short_url).first()
        if not short_url or short_url.is_expired:
            return Response("URL INVÁLIDA", status=status.HTTP_404_NOT_FOUND)

        return redirect(short_url.original_url)

