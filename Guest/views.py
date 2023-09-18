from django.shortcuts import render,redirect
from Admin.models import*

# Create your views here.
def login(request):
    if request.method=="POST":
        usercount=tbl_newuser.objects.filter(email=request.POST.get('username'),password=request.POST.get('password')).count()
        shopcount=tbl_shop.objects.filter(email=request.POST.get('username'),password=request.POST.get('password')).count()
        if usercount>0:
            userdata=tbl_newuser.objects.get(email=request.POST.get('username'),password=request.POST.get('password'))
            request.session["uid"]=userdata.id
            request.session["uname"]=userdata.name
            return redirect('webuser:home')
        elif shopcount>0:
            shopdata=tbl_shop.objects.get(email=request.POST.get('username'),password=request.POST.get('password'))
            request.session["sid"]=shopdata.id
            request.session["sname"]=shopdata.name
            return redirect('webshop:home')
        else:
            return render(request,"Guest/Login.html")
    else:
        return render(request,'Guest/Login.html')