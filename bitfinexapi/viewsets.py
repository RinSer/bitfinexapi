from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from bitfinexapi.models import Currency
from bitfinexapi.serializers import CurrencySerializer

class CurrencySetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 50

class CurrencyViewSet(viewsets.ModelViewSet):
    pagination_class = CurrencySetPagination
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer