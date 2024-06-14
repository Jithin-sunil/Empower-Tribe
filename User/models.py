from django.db import models
from Guest.models import *
from Teammember.models import *

# Create your models here.

class tbl_booking(models.Model):
    booking_date = models.DateField(auto_now_add=True)
    user=models.ForeignKey(tbl_userreg,on_delete=models.CASCADE)
    booking_status=models.IntegerField(default=0)
    booking_totalamount=models.CharField(max_length=50,null=True)

class tbl_cart(models.Model):
    booking=models.ForeignKey(tbl_booking,on_delete=models.CASCADE)
    cart_status=models.CharField(max_length=5,default='0')
    cart_qty=models.CharField(max_length=100)
    product=models.ForeignKey(tbl_product,on_delete=models.CASCADE)


class tbl_complaint(models.Model):
    user=models.ForeignKey(tbl_userreg,on_delete=models.CASCADE)
    complaint_status=models.CharField(default=0,max_length=10)
    complaint_title=models.CharField(max_length=100)
    complaint_content=models.CharField(max_length=300)
    complaint_reply=models.CharField(default='Not replied',max_length=100)
    complaint_date=models.DateField(auto_now_add=True)

class tbl_feedback(models.Model):
    user=models.ForeignKey(tbl_userreg,on_delete=models.CASCADE)
    feedback_content=models.CharField(max_length=300)
    feedback_date=models.DateField(auto_now_add=True)

class tbl_donation(models.Model):
    donation_date=models.DateField(auto_now_add=True)
    user=models.ForeignKey(tbl_userreg,on_delete=models.CASCADE)
    donation_type=models.ForeignKey(tbl_donationtype,on_delete=models.CASCADE,null=True)
    donation_details=models.CharField(max_length=50,null=True)