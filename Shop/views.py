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