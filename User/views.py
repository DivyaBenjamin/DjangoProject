from django.shortcuts import render,redirect
from User.models import*
from Admin.models import*
from Shop.models import*
from datetime import date
# Create your views here.
def home(request):
    return render(request,'User/Home.html')

def changepassword(request):
    userreg=tbl_newuser.objects.get(id=request.session['uid'])
    if request.method=="POST":
        if (userreg.password)==(request.POST.get('currentpassword')):
            if (request.POST.get('newpassword'))==(request.POST.get('confirmpassword')):
                userreg.password=request.POST.get('confirmpassword')
                userreg.save()
                return render(request,'User/Changepassword.html',{'err':3})
            else:
                return render(request,'User/Changepassword.html',{'err':1})
        else:
            return render(request,'User/Changepassword.html',{'err':2})
    else:
        return render(request,'User/Changepassword.html',{'j':userreg})

def profile(request):
    User=tbl_newuser.objects.get(id=request.session['uid'])
    return render(request,'User/Profile.html',{'i':User})

def editprofile(request):
    edituser=tbl_newuser.objects.get(id=request.session['uid'])
    if request.method=="POST":
        edituser.name=request.POST.get('name')
        edituser.contact=request.POST.get('contact')
        edituser.email=request.POST.get('email')
        edituser.address=request.POST.get('address')
        edituser.save()
        return redirect('webuser:editprofile')
    else:
        return render(request,'User/Editprofile.html',{'i':edituser})

def searchshop(request):
    district=tbl_district.objects.all()
    placedata=tbl_place.objects.all()
    shopdata=tbl_shop.objects.all()
    if request.method=="POST":
        place=tbl_place.objects.get(id=request.POST.get('place'))
        return redirect('webuser:searchshop')
    else:
        return render(request,'User/Searchshop.html',{'district':district,'shop':shopdata})

def Ajaxsearch(request):
    district=tbl_district.objects.get(id=request.GET.get('sdisd'))
    placedata=tbl_place.objects.filter(district=district)
    return render(request,'User/Ajaxsearch.html',{'place':placedata})

def Ajaxshopresult(request):
    if request.GET.get('pid')!="":
        placedata=tbl_place.objects.get(id=request.GET.get('pid'))
        shopdata=tbl_shop.objects.filter(place=placedata)
        return render(request,'User/Ajaxshopresult.html',{'shop':shopdata})
    else:
        districtdata=tbl_district.objects.get(id=request.GET.get('did'))
        shopdata=tbl_shop.objects.filter(place__district=districtdata)
        return render(request,'User/Ajaxshopresult.html',{'shop':shopdata})

def Viewmore(request,bid):
    shopdata=tbl_shop.objects.get(id=bid)
    return render(request,'User/ViewMore.html',{'k':shopdata})

def viewproducts(request):
    
    category=tbl_category.objects.all()
    subcategory=tbl_subcategory.objects.all()
    productdata=tbl_products.objects.all()
    if request.method=="POST":
        subdata=tbl_subcategory.objects.get(id=request.POST.get('subcategory'))
        return redirect('webuser:viewproducts')
    else:
        return render(request,'User/Viewproduct.html',{'category':category,'product':productdata})

def Ajaxcategory(request):
    subcategorydata=tbl_category.objects.get(id=request.GET.get('bisd'))
    productdata=tbl_subcategory.objects.filter(category=subcategorydata)
    return render(request,'User/Ajaxcategory.html',{'subcategory':productdata})

def Ajaxviewproduct(request):
    if request.GET.get('cid')!='':
        subcategorydata=tbl_subcategory.objects.get(id=request.GET.get('cid'))
        productdata=tbl_products.objects.filter(subcategory=subcategorydata)
        return render(request,'User/Ajaxviewproduct.html',{'product':productdata})
    else:
        categorydata=tbl_category.objects.get(id=request.GET.get('bid'))
        productdata=tbl_products.objects.filter(subcategory__category=categorydata)
        return render(request,'User/Ajaxviewproduct.html',{'product':productdata})

def feedback(request):
    feedbackuser=tbl_newuser.objects.get(id=request.session['uid'])
    if request.method=="POST":
        tbl_feedback.objects.create(feedback_content=request.POST.get('feedback'),user_id=feedbackuser)
        return redirect('webuser:feedback')
    else:
        return render(request,'User/Feedback.html',{'feedback':feedback})

def complaint(request):
    complaintuser=tbl_newuser.objects.get(id=request.session['uid'])
    complaintdata=tbl_complaint.objects.filter(user=complaintuser)
    if request.method=="POST":
        tbl_complaint.objects.create(description=request.POST.get('complaint'),user=complaintuser)
        return redirect('webuser:complaint')
    else:
        return render(request,'User/Complaint.html',{'complaint':complaintdata})

def viewreply(request,cid):
    reply=tbl_complaint.objects.get(id=cid)
    return render(request,'User/Viewreply.html',{'i':reply})

def productcart(request,pid):
    userdata=tbl_newuser.objects.get(id=request.session["uid"])
    productdata=tbl_products.objects.get(id=pid)
    bookingcount=tbl_booking.objects.filter(user_id=userdata,booking_status=0).count()
    if bookingcount>0:
        bookingdata=tbl_booking.objects.get(user_id=userdata,booking_status=0)
        cartcount=tbl_cart.objects.filter(booking_id=bookingdata,product_id=productdata).count()
        if cartcount>0:
            return render(request,'User/Viewproduct.html',{'msg':'Already in Cart!'})
        else:
            tbl_cart.objects.create(booking_id=bookingdata,product_id=productdata)
            return render(request,'User/Viewproduct.html',{'msg':'Added to Cart.'})
    else:
        tbl_booking.objects.create(user_id=userdata)
        bookingcount=tbl_booking.objects.filter(user_id=userdata,booking_status=0).count()
        if bookingcount>0:
            bookingdata=tbl_booking.objects.get(user_id=userdata,booking_status=0)
            cartcount=tbl_cart.objects.filter(booking_id=bookingdata,product_id=productdata).count()
            if cartcount>0:
                return render(request,'User/Viewproduct.html',{'msg':'Already in Cart!'})
            else:
                tbl_cart.objects.create(booking_id=bookingdata,product_id=productdata)
                return render(request,'User/Viewproduct.html',{'msg':'Added to Cart.'})

def mycart(request):
    userdata=tbl_newuser.objects.get(id=request.session["uid"])
    cartdata=tbl_cart.objects.filter(booking_id__user_id=userdata,booking_id__booking_status=0)
    total=0
    for i in cartdata:
        total = total+int(i.product_id.rate) * int(i.quantity)   
    return render(request,'User/Mycart.html',{'cart':cartdata,'total':total})
    

def Ajaxcart(request):
    cartdata=tbl_cart.objects.get(id=request.GET.get('cartid'))
    cartdata.quantity=request.GET.get('cdisd')
    cartdata.save()
    cartdatas=cartdata.booking_id.id
    cart=tbl_cart.objects.filter(booking_id=cartdatas)
    total1=0
    for i in cart:
        total1 = total1+int(i.quantity) * int(i.product_id.rate)
    return render(request,'User/Ajaxcart.html',{'data':total1})

def deletecart(request,did):
    tbl_cart.objects.get(id=did).delete()
    return redirect('webuser:mycart')

def payment(request):
    if request.method=="POST":
        userdata=tbl_newuser.objects.get(id=request.session["uid"])
        cartitem=tbl_cart.objects.filter(booking_id__user_id=userdata,booking_id__booking_status=0)
        booking_item=tbl_booking.objects.get(user_id=request.session["uid"],booking_status='0',payment_status='0')
        booking_item.booking_status=1
        booking_item.payment_status=1
        booking_item.save()
        balance_price=0
        for i in cartitem:
            productdata=tbl_products.objects.get(id=i.product_id.id)
            stock=productdata.stock
            balance_price = int(productdata.stock) - int(i.quantity) 
            productdata.stock=balance_price
            productdata.save()
            if productdata==0:
                userdata=tbl_newuser.objects.get(id=request.session["uid"])
                productitem=tbl_cart.objects.filter(booking_id__booking_status=0,product=product)
                for j in productitem:
                    if j.booking_id.user_id!=user_id:
                        j.quantity=0
                        j.save()
                        return redirect('webuser:paymentloader')
            else:
                return render(request,'User/Payment.html')

        return redirect('webuser:paymentloader')
    else:
        return render(request,'User/Payment.html')

def paymentloader(request):
    return render(request,'User/Loader.html')

def paymentsuc(request):
    return render(request,'User/MPayment.html')

def myorder(request):
    userdata=tbl_newuser.objects.get(id=request.session["uid"])
    data=tbl_cart.objects.filter(booking_id__user_id=userdata)
    return render(request,'User/Myorder.html',{'cart':data})

