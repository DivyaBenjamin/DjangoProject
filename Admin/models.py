from django.db import models
# Create your models here.
class tbl_district(models.Model):
    name=models.CharField(max_length=50)

class tbl_category(models.Model):
    name=models.CharField(max_length=30)

class tbl_brand(models.Model):
    name=models.CharField(max_length=45)

class tbl_place(models.Model):
    name=models.CharField(max_length=50)
    district=models.ForeignKey(tbl_district,on_delete=models.CASCADE)

class tbl_subcategory(models.Model):
    sub=models.CharField(max_length=60)
    category=models.ForeignKey(tbl_category,on_delete=models.CASCADE)

class tbl_newuser(models.Model):
    name=models.CharField(max_length=40)
    contact=models.CharField(max_length=45)
    email=models.CharField(max_length=40)
    address=models.CharField(max_length=55)
    gender=models.CharField(max_length=45)
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
    photo=models.FileField(upload_to="Userphoto/")
    password=models.CharField(max_length=45)

class tbl_shop(models.Model):
    name=models.CharField(max_length=30)
    contact=models.CharField(max_length=35)
    email=models.CharField(max_length=40)
    address=models.CharField(max_length=45)
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
    proof=models.FileField(upload_to="Shopproof/")
    photo=models.FileField(upload_to="Shopphoto/")
    password=models.CharField(max_length=40)


