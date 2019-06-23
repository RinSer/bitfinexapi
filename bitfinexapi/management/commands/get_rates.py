from decimal import Decimal
from datetime import datetime
import requests
from django.core.management.base import BaseCommand
from bitfinexapi.models import Currency, Rate

class Command(BaseCommand):
    """
    Получение курсов валют к доллару 
    за последние 10 дней (если их нет в БД)
    """

    help = 'Get bitfinex rates for all currencies'

    def handle(self, *args, **options):
        currencies = Currency.objects.all()
        for currency in currencies:
            get_rates_for(currency)

BITFINEXURL = 'https://api-pub.bitfinex.com/v2/candles/trade:1D:t%sUSD/hist?limit=%s'

def get_rates_for(currency):
    last_rate = Rate.objects.filter(currency=currency)\
        .order_by('-date').first()
    limit = 10
    if last_rate:
        limit = datetime.now().day - last_rate.date.day
    if limit > 0:
        currency_url = BITFINEXURL % (currency.name, limit)
        response = requests.get(currency_url)
        if response.status_code == 200:
            candles = response.json()
            if len(candles) > 0:
                Rate.objects.bulk_create(map(
                    lambda candle: Rate(
                        currency=currency,
                        date=datetime.fromtimestamp(int(candle[0])/1000.0),
                        rate=Decimal(candle[2]),
                        volume=Decimal(candle[5])
                    ), candles
                ))