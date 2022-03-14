from django.shortcuts import render,redirect
from pyparsing import empty
from home.models import cake
from django.core.cache import cache
from . models import comment

# Create your views here.

def details(request):
    if request.method=='POST':
        cmt=request.POST['cmt']

        uname=request.POST['uname']
        id = request.POST ['id']

        object = comment.objects.create(cakes_id =id,name=uname,messsage=cmt)
        object.save();
       
        #page loading values
        pro=cake.objects.get(id=id)
        price = pro.price
        discount = pro.offer
        discount_price = price*(discount/100)
        actual_price = pro.price - discount_price
        return render(request,'single-product.html',{'product':pro,'actp':actual_price})
    else:

    
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
    

def comments(request):
    
    cmt=request.GET['cmt']

    uname=request.GET['uname']
    id = request.GET['id']

    object = comment.objects.create(cakes_id =id,name=uname,messsage=cmt)
    object.save();
    return redirect('/')

    

   

    return render(request,'savi.html',{'cmt':cmt})



    
    
    
    

   
