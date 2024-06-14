from django.db import models
from Admin.models import *
# Create your models here.

class tbl_family(models.Model):
    teammember=models.ForeignKey(tbl_teammember,on_delete=models.CASCADE)
    family_housename=models.CharField(max_length=50)
    family_address=models.CharField(max_length=50)
    family_member_count=models.CharField(max_length=50,null=True)
    

class tbl_familymember(models.Model):
    family=models.ForeignKey(tbl_family,on_delete=models.CASCADE)
    family_member_name=models.CharField(max_length=50)
    family_member_gender=models.CharField(max_length=50)
    family_member_age=models.CharField(max_length=50)
    family_member_relation=models.CharField(max_length=50)
    
class tbl_product(models.Model):
    member=models.ForeignKey(tbl_teammember,on_delete=models.CASCADE)
    product_name=models.CharField(max_length=50)  
    product_price=models.CharField(max_length=50) 
    product_details=models.CharField(max_length=50) 
    product_image=models.FileField(upload_to='ProductDoc/')
    product_date=models.DateField(auto_now_add=True)
    product_category=models.ForeignKey(tbl_category,on_delete=models.CASCADE)
    family=models.ForeignKey(tbl_family,on_delete=models.CASCADE,null=True)

class tbl_stock(models.Model):
    product=models.ForeignKey(tbl_product,on_delete=models.CASCADE)
    stock_date=models.DateField(auto_now_add=True)
    stock_qty=models.CharField(max_length=50)
   

class tbl_familyneedlist(models.Model):
    family=models.ForeignKey(tbl_family,on_delete=models.CASCADE)
    donationtype=models.ForeignKey(tbl_donationtype,on_delete=models.CASCADE)
    need=models.CharField(max_length=50)
    need_status=models.IntegerField(default=0,null=True)
    