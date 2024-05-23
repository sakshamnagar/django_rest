from rest_framework import serializers

from apps.markets.models import Market



class MarketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Market
        fields = ('id', 'name', 'vendors',)