from django.db import models
from Admin.models import*
from Shop.models import*
# Create your models here.
class tbl_booking(models.Model):
    booking_status=models.CharField(max_length=1,default='0')
    user_id=models.ForeignKey(tbl_newuser,on_delete=models.CASCADE)
    status=models.CharField(max_length=1,default='0')
    payment_status=models.CharField(max_length=1,default='0')
    booking_date=models.DateField(auto_now_add=True,null=True)

class tbl_cart(models.Model):
    quantity=models.IntegerField(default=1)
    product_id=models.ForeignKey(tbl_products,on_delete=models.CASCADE)
    booking_id=models.ForeignKey(tbl_booking,on_delete=models.CASCADE)
    status=models.CharField(max_length=1,default='0')

class tbl_feedback(models.Model):
    feedback_content=models.CharField(max_length=40)
    feedback_date=models.DateField(auto_now_add=True)
    user_id=models.ForeignKey(tbl_newuser,on_delete=models.SET_NULL,null=True)
    shop_id=models.ForeignKey(tbl_shop,on_delete=models.SET_NULL,null=True)

class tbl_complaint(models.Model):
    user=models.ForeignKey(tbl_newuser,on_delete=models.SET_NULL,null=True)
    shop=models.ForeignKey(tbl_shop,on_delete=models.SET_NULL,null=True)
    description=models.CharField(max_length=45)
    complaint_date=models.DateField(auto_now_add=True)
    reply=models.CharField(max_length=50,default='No reply')
    status=models.CharField(max_length=1,default='0')
    
class tbl_rating(models.Model):
    ratingdata=models.IntegerField()
    user=models.ForeignKey(tbl_newuser,on_delete=models.SET_NULL,null=True)
    product=models.ForeignKey(tbl_products,on_delete=models.SET_NULL,null=True)
    opinion=models.CharField(max_length=50)
    