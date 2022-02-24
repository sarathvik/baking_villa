from django.shortcuts import render
from django.http import HttpResponse
from . models import cake

# Create your views here.
product1 = cake()
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
product3.image = 'cake3.jpg'

product4 = cake()
product4.name = 'cake4'
product4.price = 2500
product4.image = 'cake4.jpg'

product = [product1,product2,product3,product4] 




def index(request):
    return render(request,'index.html',{'proname':product})

   


   
