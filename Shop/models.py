from django.db import models
from Admin.models import*
# Create your models here.
class tbl_products(models.Model):
    name=models.CharField(max_length=50)
    rate=models.CharField(max_length=30)
    image=models.FileField(upload_to="Productpic/")
    stock=models.CharField(max_length=35)
    shop=models.ForeignKey(tbl_shop,on_delete=models.CASCADE)
    subcategory=models.ForeignKey(tbl_subcategory,on_delete=models.CASCADE)
    status=models.CharField(max_length=1,default='0')