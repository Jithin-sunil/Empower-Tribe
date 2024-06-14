from django.db import models


# Create your models here.

class tbl_localbodytype(models.Model):
    localbodytype_name = models.CharField(max_length=50)

class tbl_localbody(models.Model):
    localbodytype=models.ForeignKey(tbl_localbodytype,on_delete=models.CASCADE)    
    localbody= models.CharField(max_length=50)

class tbl_ward(models.Model):
    localbody=models.ForeignKey(tbl_localbody,on_delete=models.CASCADE)    
    ward= models.CharField(max_length=50)

class tbl_donationtype(models.Model):
    donationtype = models.CharField(max_length=50)    

class tbl_team(models.Model):
    team_name=models.CharField(max_length=50)
    member_count = models.CharField(max_length=50)   
     
class tbl_assigmment(models.Model):
    team=models.ForeignKey(tbl_team,on_delete=models.CASCADE,null=True)
    ward=models.ForeignKey(tbl_ward,on_delete=models.CASCADE,null=True) 

class tbl_teammember(models.Model):
    assignment=models.ForeignKey(tbl_assigmment,on_delete=models.CASCADE,null=True)
    member_name=models.CharField(max_length=50) 
    member_contact=models.CharField(max_length=50) 
    member_email=models.CharField(max_length=50)
    member_address=models.CharField(max_length=50)
    member_photo=models.FileField(upload_to='Memberdoc/')
    member_proof=models.FileField(upload_to='Memberproof/')
    member_password=models.CharField(max_length=50)  
    member_status=models.IntegerField(default=0,null=True)
        
class tbl_category(models.Model):
    category_name = models.CharField(max_length=50)

class tbl_registration(models.Model):
    registration_name=models.CharField(max_length=50) 
    registration_contact=models.CharField(max_length=50) 
    registration_email=models.CharField(max_length=50)
    registration_password=models.CharField(max_length=50)    