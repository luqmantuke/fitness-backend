from rest_framework import serializers

from .models import BannerImages


class BannerImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BannerImages
        fields = ['image_field']
