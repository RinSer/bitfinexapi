from django.contrib.auth.models import User
from rest_framework import serializers
from bitfinexapi.models import Currency, Rate

class CurrencySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Currency
        fields = ('id', 'name')