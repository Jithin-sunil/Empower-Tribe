from django.db import models

# Create your models here.
class tbl_userreg(models.Model):
    userregistration_name=models.CharField(max_length=50) 
    userregistration_contact=models.CharField(max_length=50) 
    userregistration_email=models.CharField(max_length=50)
    userregistration_address=models.CharField(max_length=50)
    userregistration_photo=models.FileField(upload_to='UserDoc/')
    userregistration_proof=models.FileField(upload_to='UserDoc/') 
    userregistration_password=models.CharField(max_length=50)

    