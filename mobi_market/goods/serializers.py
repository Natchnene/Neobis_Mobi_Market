from rest_framework import serializers
from .models import CardProduct


class CardProductLongSerializer(serializers.ModelSerializer):
    all_likes = serializers.SerializerMethodField()

    def get_all_likes(self, obj):
        return obj.all_likes()

    class Meta:
        model = CardProduct
        fields = ['id', 'title', 'price', 'photo', 'short_description', 'long_description', 'user', 'likes', 'all_likes']


class CardProductShortSerializer(serializers.ModelSerializer):
    all_likes = serializers.SerializerMethodField()

    def get_all_likes(self, obj):
        return obj.all_likes()

    class Meta:
        model = CardProduct
        fields = ['id', 'title', 'price', 'photo', 'short_description', 'user', 'likes', 'all_likes']

