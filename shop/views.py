from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Contact,Orders,OrderUpdate
from math import ceil
import json
from django.contrib.auth.decorators import login_required
from django.conf import settings


def index(request):

    all_product=[]
    catagory=Product.objects.values('catagory','id')
    filter_catagory={item['catagory'] for item in catagory}
    for cat in filter_catagory:
        prod=Product.objects.filter(catagory=cat)

        n = len(prod)
        nSlide = n // 4 + ceil((n / 4) - (n // 4))
        all_product.append([prod,range(1,nSlide),nSlide,cat])

    l = {"all_product": all_product}
    return render(request,'shop/home.html',l)

def about(request):


    return render(request,'shop/about.html')


def contact(request):
    thank=False
    if request.method=="POST":
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        desc=request.POST.get('desc','')
        contacts=Contact(name=name,email=email,phone=phone,desc=desc)
        contacts.save()
        thank=True

    return render(request,'shop/contact.html',{'thank':thank})

def tracker(request):
    if request.method=="POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Orders.objects.filter(order_id=orderId, email=email)
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps({"status":"success", "updates": updates, "itemsJson": order[0].item_json}, default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{"status":"noitem"}')
        except Exception as e:
            return HttpResponse('{"status":"error"}')

    return render(request, 'shop/tracker.html')







def searchMatch(query, item):
    '''return true only if query matches the item'''
    if query in item.description.lower() or query in item.product_name.lower() or query in item.catagory.lower():
        return True
    else:
        return False

def search(request):
    query = request.GET.get('search')
    allProds = []
    catprods = Product.objects.values('catagory', 'id')
    cats = {item['catagory'] for item in catprods}
    for cat in cats:
        prodtemp = Product.objects.filter(catagory=cat)
        prod = [item for item in prodtemp if searchMatch(query, item)]

        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        if len(prod) != 0:
            allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds': allProds, "msg": ""}
    if len(allProds) == 0 or len(query)<2:
        params = {'msg': "Please make sure to enter relevant search query"}
    return render(request, 'shop/search.html', params)



def prodview(request,id):
    product=Product.objects.filter(id=id)
    return render(request,'shop/prodview.html',{'product':product[0]})

@login_required
def checkout(request):
    if request.method=="POST":
        item_json = request.POST.get('itemsJson', '')
        name=request.POST.get('name','')
        amount=request.POST.get('amount','')
        email=request.POST.get('email','')
        address=request.POST.get('address1','')+ ' ' +request.POST.get('address2','')
        city=request.POST.get('city','')
        state=request.POST.get('state','')
        zip_code=request.POST.get('zip_code','')
        phone=request.POST.get('phone','')
        order=Orders(name=name,email=email,address=address,city=city,state=state,zip_code=zip_code,phone=phone,item_json=item_json,amount=amount)
        order.save()
        update = OrderUpdate(order_id=order.order_id, update_desc="The order has been placed")
        update.save()
        thank = True
        id = order.order_id
        return render(request, 'shop/cheakout.html', {'thank': thank, 'id': id})
    return render(request,'shop/cheakout.html')


