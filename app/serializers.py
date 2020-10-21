from app.models import user, item
from aiohttp_rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = item
        fields = '__all__'
