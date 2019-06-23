from django.http import Http404
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from bitfinexapi.models import Rate

class RateView(APIView):
    """
    Возвращает текущий курс валюты к доллару
    """

    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None, cid=None):
        try:
            last_rates = Rate.objects.filter(currency_id=cid)\
                .order_by('-date')[:10]
            
            return Response({
                'currency' : last_rates[0].currency.name,
                'rate' : last_rates[0].rate,
                'volume' : sum(r.volume for r in last_rates) / len(last_rates)
            })
        except Exception:
            raise Http404