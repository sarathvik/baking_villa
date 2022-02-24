from django.db import models

# Create your models here.
class cake(models.Models):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pics')
    price = models.IntegerField()
    stock = models.FloatField()
    
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    offer = models.FloatField()
    offer_offer2 = models.BooleanField(default=False)
    



