from rest_framework import serializers
from .models import Madini


class MadiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Madini
        fields = ('id', 'title', 'content', 'images','created_at','published')

