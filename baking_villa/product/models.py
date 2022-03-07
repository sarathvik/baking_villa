from django.db import models
from home.models import cake



# Create your models here.
class comment(models.Model):
    cakes = models.ForeignKey(cake,related_name = "comments",on_delete=models.CASCADE)
    
    name = models.CharField(max_length=100)
    messsage = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    