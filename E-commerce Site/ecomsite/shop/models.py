from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    discount_price = models.FloatField()
    category = models.CharField(max_length=200)
    desc = models.TextField()
    image = models.CharField(max_length=300)
    

    def __str__(self) -> str:
        return self.title