# Generated by Django 2.0.5 on 2019-06-23 15:17

from django.db import migrations

CURRENCIES = [
    'BTC',
    'ETH',
    'LTC',
    'XRP',
    'OMG'
]

def seed_currencies(apps, schema_editor):
    Currency = apps.get_model('bitfinexapi', 'Currency')
    Currency.objects.bulk_create(map(
        lambda name: Currency(name=name), CURRENCIES
    ))

class Migration(migrations.Migration):

    dependencies = [
        ('bitfinexapi', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed_currencies)
    ]
