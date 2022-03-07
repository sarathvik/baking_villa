from django.shortcuts import render
from django.http import HttpResponse
from . models import cake

# Create your views here.
'''product1 = cake()
product1.name = 'cake1'
product1.price = 1000
product1.image = 'cake1.jpg'

product2 = cake()
product2.name = 'cake2'
product2.price = 1500
product2.image = 'cake2.jpg'

product3 = cake()
product3.name = 'cake3'
product3.price = 2000
product3.image = 'cake3.jpg'''






def index(request):
    product = cake.objects.all()
    
    return render(request,'index.html',{'proname':product})

   


   
