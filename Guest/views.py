from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *

# Create your views here.
def Login(request):
    if request.method=="POST":
       login_email=request.POST.get("txtemail")
       login_password=request.POST.get("txtpassword")

       membercount = tbl_teammember.objects.filter(member_email=login_email,member_password=login_password,member_status=1).count() 
       member_s0=tbl_teammember.objects.filter(member_email=login_email,member_password=login_password,member_status=0).count()
       member_s2=tbl_teammember.objects.filter(member_email=login_email,member_password=login_password,member_status=2).count()
       usercount = tbl_userreg.objects.filter(userregistration_email=login_email,userregistration_password=login_password).count() 
       admincount = tbl_registration.objects.filter(registration_email=login_email,registration_password=login_password).count() 
       
       if membercount > 0:
          member = tbl_teammember.objects.get(member_email=login_email,member_password=login_password)
          request.session["mid"] = member.id
          return redirect("Webteammember:homepage")
       elif member_s0>0:
          membermsg0="pending"
          return render(request,"Guest/Login.html",{'membermsg1':membermsg0})
       elif member_s2>0:
          membermsg2="rejected"
          return render(request,"Guest/Login.html",{'membermsg':membermsg2})
       elif usercount > 0:
          user = tbl_userreg.objects.get(userregistration_email=login_email,userregistration_password=login_password)
          request.session["uid"] = user.id
          return redirect("Webuser:homepage")
       elif admincount > 0:
          admin = tbl_registration.objects.get(registration_email=login_email,registration_password=login_password)
          request.session["aid"] = admin.id
          return redirect("Webadmin:homepage")  
    else:                                           
        return render(request,"Guest/Login.html",{"msg":"error"})
    

def UserRegistration(request):
    if request.method=="POST":
      
      tbl_userreg.objects.create(userregistration_name=request.POST.get('txtname'),
                                       userregistration_contact=request.POST.get('txtnumber'),
                                       userregistration_email=request.POST.get('txtemail'),
                                       userregistration_address=request.POST.get('txtaddress'),
                                       userregistration_photo=request.FILES.get('Photo'),
                                       userregistration_password=request.POST.get('txtpassword'),
                                       userregistration_proof=request.POST.get('Proof')
                                       )
      return render(request,"Guest/UserRegistration.html")
    else:
      return render(request,"Guest/UserRegistration.html")    
    


def MemberRegistration(request,id):
    memberdata=tbl_teammember.objects.all()
    if request.method=="POST":
      tbl_teammember.objects.create(member_name=request.POST.get('txtname'),
                                       member_contact=request.POST.get('txtnumber'),
                                       member_email=request.POST.get('txtemail'),
                                       member_address=request.POST.get('txtaddress'),
                                       member_photo=request.FILES.get('Photo'),
                                       member_proof=request.FILES.get('Proof'),
                                       member_password=request.POST.get('txtpassword1'),
                                       assignment=tbl_assigmment.objects.get(id=id)
                                       )
      return render(request,"Guest/Add_members.html",{memberdata:memberdata})   
    else:
      return render(request,"Guest/Add_members.html",{memberdata:memberdata})
    
def ViewTeams(request):
    team=tbl_assigmment.objects.all()
    return render(request,"Guest/ViewTeams.html",{"data":team})   



