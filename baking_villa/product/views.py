from django.shortcuts import render,redirect
from home.models import cake
from django.core.cache import cache

# Create your views here.

def details(request):

    
    id=request.GET['id']
    if cache.get(id):
        print("data from cache")
        pro = cache.get(id)
        price = pro.price
        discount = pro.offer
        discount_price = price*(discount/100)
        actual_price = pro.price - discount_price
    else:    

        pro = cake.objects.get(id=id)
        cache.set(id,pro)
        print("data from database")
        price = pro.price
        discount = pro.offer
        discount_price = price*(discount/100)
        actual_price = pro.price - discount_price
    


    return render(request,'single-product.html',{'product':pro,'actp':actual_price})
    

    
    
    
    
    

   
