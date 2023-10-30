from django.shortcuts import render,redirect
from Admin.models import *
from User.models import *
# Create your views here.

def district(request):
    disdata=tbl_district.objects.all()
    if request.method=="POST":
        tbl_district.objects.create(name=request.POST.get('district'))
        return redirect('webadmin:district')
    else:
        return render(request,'Admin/District.html',{'dis':disdata})

def deletedis(request,did):
    tbl_district.objects.get(id=did).delete()
    return redirect('webadmin:district')

def editdistrict(request,eid):
    editdata=tbl_district.objects.get(id=eid)
    if request.method=="POST":
        editdata.name=request.POST.get('district')
        editdata.save()
        return redirect('webadmin:district')
    else:
        return render(request,'Admin/District.html',{'data':editdata})

def category(request):
    catdata=tbl_category.objects.all()
    if request.method=="POST":
        tbl_category.objects.create(name=request.POST.get('category'))
        return redirect('webadmin:category')
    else:
        return render(request,'Admin/Category.html',{'cat':catdata})

def deletecat(request,cid):
    tbl_category.objects.get(id=cid).delete()
    return redirect('webadmin:category')

def editcategory(request,fid):
    editdata=tbl_category.objects.get(id=fid)
    if request.method=="POST":
        editdata.name=request.POST.get('category')
        editdata.save()
        return redirect('webadmin:category')
    else:
        return render(request,'Admin/Category.html',{'data':editdata})

def brand(request):
    branddata=tbl_brand.objects.all()
    if request.method=="POST":
        tbl_brand.objects.create(name=request.POST.get('brand'))
        return redirect('webadmin:brand')
    else:
        return render(request,'Admin/Brand.html',{'brand':branddata})

def deletebrand(request,bid):
    tbl_brand.objects.get(id=bid).delete()
    return redirect('webadmin:brand')

def editbrand(request,gid):
    editbrand=tbl_brand.objects.get(id=gid)
    if request.method=="POST":
        editbrand.name=request.POST.get('brand')
        editbrand.save()
        return redirect('webadmin:brand')
    else:
        return render(request,'Admin/Brand.html',{'data':editbrand})

def place(request):
    district=tbl_district.objects.all()
    placedata=tbl_place.objects.all()
    if request.method=="POST":
        dis=tbl_district.objects.get(id=request.POST.get('district'))
        tbl_place.objects.create(name=request.POST.get('place'),district=dis)
        return redirect('webadmin:place')
    else:
        return render(request,'Admin/Place.html',{'dis':district,'place':placedata})

def deleteplace(request,jid):
    tbl_place.objects.get(id=jid).delete()
    return redirect('webadmin:place')

def subcategory(request):
    category=tbl_category.objects.all()
    subdata=tbl_subcategory.objects.all()
    if request.method=="POST":
        sub=tbl_category.objects.get(id=request.POST.get('Category'))
        tbl_subcategory.objects.create(sub=request.POST.get('subcategory'),category=sub)
        return redirect('webadmin:subcategory')
    else:
        return render(request,'Admin/Subcategory.html',{'cat':category,'subcategory':subdata})
        
def deletesub(request,hid):
    tbl_subcategory.objects.get(id=hid).delete()
    return redirect('webadmin:subcategory')

def newuser(request):
    district=tbl_district.objects.all()
    if request.method=="POST":
        place=tbl_place.objects.get(id=request.POST.get('place'))  
        tbl_newuser.objects.create(name=request.POST.get('name'),contact=request.POST.get('contact'),email=request.POST.get('email'),address=request.POST.get('address'),gender=request.POST.get('gender'),place=place,photo=request.FILES.get('photo'),password=request.POST.get('password'))
        return redirect('webadmin:newuser')
    else:
        return render(request,'Admin/Newuser.html',{'district':district})

def Ajaxplace(request):
    dis=tbl_district.objects.get(id=request.GET.get('disd'))
    place=tbl_place.objects.filter(district=dis)
    return render(request,'Admin/Ajaxplace.html',{'place':place})

def shop(request):
    district=tbl_district.objects.all()
    if request.method=="POST":
        place=tbl_place.objects.get(id=request.POST.get('place'))
        tbl_shop.objects.create(name=request.POST.get('shopname'),contact=request.POST.get('shopcontact'),email=request.POST.get('shopemail'),address=request.POST.get('shopaddress'),place=place,proof=request.FILES.get('proof'),photo=request.FILES.get('photo'),password=request.POST.get('password'))
    return render(request,'Admin/Shop.html',{'district':district})

def Ajaxshop(request):
    dis=tbl_district.objects.get(id=request.GET.get('disd'))
    place=tbl_place.objects.filter(district=dis)
    return render(request,'Admin/Ajaxshop.html',{'place':place})

def viewfeedback(request):
    user=tbl_newuser.objects.all()
    feedbackdata=tbl_feedback.objects.filter(user_id__in=user)
    shop=tbl_shop.objects.all()
    shopfeedback=tbl_feedback.objects.filter(shop_id__in=shop)
    return render(request,'Admin/Viewfeedback.html',{'feedback':shopfeedback,'feedback1':feedbackdata})

def viewcomplaint(request):
    user=tbl_newuser.objects.all()
    complaintdata=tbl_complaint.objects.filter(user__in=user)
    shop=tbl_shop.objects.all()
    shopcomplaint=tbl_complaint.objects.filter(shop__in=shop)
    return render(request,'Admin/Viewcomplaint.html',{'complaint':shopcomplaint,'complaint1':complaintdata})

def reply(request,kid):
    complaint=tbl_complaint.objects.get(id=kid)
    if request.method=="POST":
        complaint.reply=request.POST.get('reply')
        complaint.status=1
        complaint.save()
        return redirect('webadmin:viewcomplaint')
    else:
        return render(request,'Admin/Reply.html',{'complaint':complaint,'complaint1':complaint})

def viewreport(request):
    shopdata=tbl_shop.objects.all()
    product=[]
    for i in shopdata:
        data=tbl_cart.objects.filter(product_id__shop_id=i.id,booking_id__booking_status=2).count()
        product.append(data)
    datas=zip(shopdata,product)
    return render(request,"Admin/Viewreport.html",{'product':datas})

def shopreport(request):
    shopdata=tbl_shop.objects.all()
    return render(request,'Admin/Shopreport.html',{'product':shopdata})

def viewreportshop(request,lid):
    shopdata=tbl_shop.objects.get(id=lid)
    productdata=tbl_products.objects.filter(shop=shopdata)
    ratingdata=tbl_rating.objects.all()
    rate=[]
    ar=[1,2,3,4,5]
    for i in productdata:
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
    content=zip(productdata,rate)
    return render(request,'Admin/Viewreportshop.html',{'product':content,'ar':ar})
    