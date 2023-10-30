from django.shortcuts import render,redirect
from User.models import*
from Admin.models import*
from Shop.models import*
from datetime import date
# Create your views here.

def home(request):
    return render(request,'Shop/Home.html')

def products(request):
    category=tbl_category.objects.all()
    productdata=tbl_products.objects.all()
    if request.method=="POST":
        subcategory=tbl_subcategory.objects.get(id=request.POST.get('subcategory'))
        shopdata=tbl_shop.objects.get(id=request.session["sid"])
        tbl_products.objects.create(name=request.POST.get('name'),rate=request.POST.get('rate'),image=request.FILES.get('image'),stock=request.POST.get('stock'),subcategory=subcategory,shop=shopdata)
        return render(request,'Shop/Products.html',{'category':category})
    else:
        return render(request,'Shop/Products.html',{'category':category,'product':productdata})


def Ajaxproduct(request):
   category=tbl_category.objects.get(id=request.GET.get('pisd'))
   subcategory=tbl_subcategory.objects.filter(category=category)
   return render(request,'Shop/Ajaxproduct.html',{'subcategory':subcategory})

def deleteproduct(request,pid):
    tbl_products.objects.get(id=pid).delete()
    return redirect('webshop:products')

def updatestock(request,rid):
    updatestock=tbl_products.objects.get(id=rid)
    if request.method=="POST":
        oldstock=updatestock.stock
        newstock=request.POST.get('stock')
        tot=int(oldstock)+int(newstock)
        updatestock.stock=tot
        updatestock.save()
        return redirect('webshop:products')
    else:
        return render(request,'Shop/Updatestock.html',{'i':updatestock})

def feedback(request):
    feedbackshop=tbl_shop.objects.get(id=request.session['sid'])
    if request.method=="POST":
        tbl_feedback.objects.create(feedback_content=request.POST.get("feedback"),shop_id=feedbackshop)
        return redirect('webshop:feedback')
    else:
        return render(request,'Shop/Feedback.html',{'feedback':feedback})

def complaint(request):
    complaintshop=tbl_shop.objects.get(id=request.session['sid'])
    complaintdata=tbl_complaint.objects.filter(shop=complaintshop)
    if request.method=="POST":
        tbl_complaint.objects.create(description=request.POST.get("shopcomplaint"),shop=complaintshop)
        return redirect('webshop:complaint')
    else:
        return render(request,'Shop/Complaint.html',{'complaint':complaintdata})

def viewreply(request,sid):
    reply=tbl_complaint.objects.get(id=sid)
    return render(request,'Shop/Complaint.html')

def userorders(request):
    shopdata=tbl_shop.objects.get(id=request.session['sid'])
    data=tbl_cart.objects.filter(product_id__shop=shopdata,booking_id__booking_status=1)
    return render(request,'Shop/Userorders.html',{'cart':data})

def updateorder(request,tid):
    booking_item=tbl_booking.objects.get(id=tid)
    booking_item.booking_status=2
    booking_item.save()
    return render(request,'Shop/Userorders.html')

def updatereject(request,uid):
    booking_item=tbl_booking.objects.get(id=uid)
    booking_item.booking_status=3
    booking_item.save()
    return render(request,'Shop/Userorders.html')

def report(request):
    if request.method=="POST":
        shopdata=tbl_shop.objects.get(id=request.session['sid'])
        fromdate=request.POST.get("fromdate")
        todate=request.POST.get("todate")
        if fromdate!="" and todate!="":
            productdata=tbl_cart.objects.filter(booking_id__booking_date__gte=fromdate,booking_id__booking_date__lte=todate,
                                                product_id__shop=shopdata)
            return render(request,"Shop/Report.html",{'product':productdata})
        elif fromdate!="":
            productdata=tbl_cart.objects.filter(booking_id__booking_date__gte=fromdate,
                                                product_id__shop=shopdata)
            return render(request,"Shop/Report.html",{'product':productdata})
        else:
            productdata=tbl_cart.objects.filter(booking_id__booking_date__lte=todate,
                                                product_id__shop=shopdata)
            return render(request,"Shop/Report.html",{'product':productdata})
    return render(request,'Shop/Report.html')

def bookingreport(request):
    return render(request,"Shop/Bookingreport.html")

def Ajaxfromdatereport(request):
    shopdata=tbl_shop.objects.get(id=request.session['sid'])
    fromdate=request.GET.get("risd")
    todate=request.GET.get("bisd")
    if fromdate!="" and todate!="":
        productdata=tbl_cart.objects.filter(booking_id__booking_date__gte=fromdate,booking_id__booking_date__lte=todate,
                                                product_id__shop=shopdata)
        return render(request,"Shop/Ajaxfromdatereport.html",{'product':productdata})
    elif fromdate!="":
        productdata=tbl_cart.objects.filter(booking_id__booking_date__gte=fromdate,
                                                product_id__shop=shopdata)
        return render(request,"Shop/Ajaxfromdatereport.html",{'product':productdata})
    else:
        productdata=tbl_cart.objects.filter(booking_id__booking_date__lte=todate,
                                                product_id__shop=shopdata)
        return render(request,"Shop/Ajaxfromdatereport.html",{'product':productdata})

def viewrating(request):
    ratingdata=tbl_rating.objects.all()
    rate=[]
    ar=[1,2,3,4,5]
    shop=tbl_shop.objects.get(id=request.session["sid"])
    data=tbl_products.objects.filter(shop=shop)
    for i in data:
        product=tbl_products.objects.get(id=i.id)
        ratecount=tbl_rating.objects.filter(product=product).count()
        if ratecount>0:
            ratingdata=tbl_rating.objects.filter(product=product)
            total=0
            average=0
            for j in ratingdata:
                total=total+j.ratingdata
            average=total/ratecount
            rate.append(average)
        else:
            rate.append(0)
    #print(rate)
    content=zip(data,rate)
    return render(request,'Shop/Viewrating.html',{'product':content,'ar':ar})

def Ajaxviewproduct(request):
    return render (request,'Shop/Ajaxviewproduct.html')