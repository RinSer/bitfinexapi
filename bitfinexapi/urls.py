from django.conf.urls import url, include
from rest_framework import serializers, viewsets, routers
from bitfinexapi.viewsets import CurrencyViewSet
from bitfinexapi.views import RateView

router = routers.DefaultRouter()
router.register(r'currencies', CurrencyViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url('^rate/(?P<cid>\d+)/$', RateView.as_view()),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]