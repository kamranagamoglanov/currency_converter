from django.db import models

# Create your models here.
class Currency(models.Model):
    CURRENCY = (
    ("AZN", "AZN"),
    ("USD", "USD"),
    ("EUR", "EUR" ),
    )
    from_currency= models.CharField("Currency", max_length=3, choices=CURRENCY, null=True, blank=True)
    to_currency= models.CharField("Currency", max_length=3, choices=CURRENCY, null=True, blank=True)
    amount = models.FloatField()

    def __str__(self) -> str:
        return f"{self.from_currency}"
    



