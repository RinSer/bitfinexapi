from django.db import models

class Currency(models.Model):
    """
    Валюта
    """
    name = models.CharField(max_length=125)

class Rate(models.Model):
    """
    Курс к доллару
    """
    currency = models\
        .ForeignKey(Currency, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=False, blank=False)
    rate = models.DecimalField(decimal_places=2, max_digits=7)
    volume = models.DecimalField(decimal_places=2, max_digits=25)