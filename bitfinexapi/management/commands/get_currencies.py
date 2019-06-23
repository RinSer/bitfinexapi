import requests
from django.core.management.base import BaseCommand
from bitfinexapi.models import Currency


class Command(BaseCommand):
    """
    Получить все валюты, обмениваемые на доллар
    """

    help = 'Get all currencies trade with dollar'

    def handle(self, *args, **options):
        get_currencies()

BITFINEXURL = 'https://api.bitfinex.com/v1/symbols'

def get_currencies():
    response = requests.get(BITFINEXURL)
    if response.status_code == 200:
        for symbol in response.json():
            if symbol[3:] == 'usd':
                name = symbol[:3].upper()
                if len(Currency.objects.filter(name=name)) == 0:
                    currency = Currency(name=name)
                    currency.save()