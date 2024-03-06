from django.db import models

# Create your models here.

class Stock(models.Model):
    symbol = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    last_price = models.FloatField()
    date_added = models.DateTimeField(auto_now_add=True) #date and time stock was added to database
    volume = models.BigIntegerField()

    def __str__(self):
        return self.symbol

class SMAIndicator(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    date = models.DateField() #date for which SMA value is calculated
    period = models.IntegerField()  # example: 20 for 20-day SMA
    value = models.FloatField() #calculated SMA

    def __str__(self):
        return f"{self.stock.symbol} SMA{self.period} - {self.date}: Value={self.value}"
