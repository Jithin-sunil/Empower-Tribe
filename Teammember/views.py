from django.shortcuts import render,redirect
from Teammember.models import *
from Admin.models import *
from User.models import *
from django.db.models import Sum
# Create your views here.

def homepage(request):
    return render(request,"Teammember/Homepage.html")

def MyProfile(request): 
    myprofile=tbl_teammember.objects.get(id=request.session["mid"] )
    return render(request,"Teammember/Myprofile.html",{'data':myprofile})

def EditProfile(request): 
    myprofile=tbl_teammember.objects.get(id=request.session["mid"] )
    if request.method=="POST":
        myprofile.member_name=request.POST.get("txtname")
        myprofile.member_email=request.POST.get("txtemail")
        myprofile.member_contact=request.POST.get("txtcontact")
        myprofile.member_address=request.POST.get("txtaddress")
        myprofile.save()
        return redirect("Webteammember:myprofile")
    else:
        return render(request,"Teammember/EditProfile.html",{'data':myprofile})

def ChangePassword(request): 
    myprofile=tbl_teammember.objects.get(id=request.session["mid"] )
    new=request.POST.get("txtpassword1")
    current=request.POST.get("currentpassword")
    confirm=request.POST.get("txtpassword2")
    old=myprofile.userregistration_password
    if request.method=="POST":
        if old == current:
            if new == confirm:
                myprofile.userregistration_password=new
                myprofile.save()
                msg="Password Changed"
                return render(request,"Teammember/ChangePassword.html",{'msg':msg})   
            else:
                msg="Password mismatch"
                return render(request,"Teammember/ChangePassword.html",{'msg':msg})   
        else:
            msg="Wrong Old Password"
            return render(request,"Teammember/ChangePassword.html",{'msg':msg}) 
    else:
        return render(request,"Teammember/ChangePassword.html") 

def family(request):
    data=tbl_family.objects.filter(teammember=tbl_teammember.objects.get(id=request.session["mid"]))
    if request.method == "POST":
        tbl_family.objects.create(teammember=tbl_teammember.objects.get(id=request.session["mid"]),
        family_housename=request.POST.get("txt_housename"),
        family_address=request.POST.get("txt_address"),
        family_member_count=request.POST.get("txt_count")
        )
        return redirect("Webteammember:family")
    else:
        return render(request,"Teammember/Add_family.html",{"data":data})
    
def familymembers(request,id):  
    data=tbl_familymember.objects.filter(family=tbl_family.objects.get(id=id))
    if request.method == "POST":
        tbl_familymember.objects.create(family=tbl_family.objects.get(id=id),
        family_member_name=request.POST.get("txt_name"),
        family_member_relation=request.POST.get("txt_relation"),
        family_member_age=request.POST.get("txt_age"),
        family_member_gender=request.POST.get("Gender"))
        return redirect("Webteammember:family")
    else:
        return render(request,"Teammember/Add_Familymembers.html",{"data":data})
    

def Product(request,id):
    category=tbl_category.objects.all()
    if request.method=="POST":
        tbl_product.objects.create(product_name=request.POST.get("txtname"),
                                  product_price=request.POST.get("txtprice"),
                                  product_details=request.POST.get("txtdetails"),
                                  product_category=tbl_category.objects.get(id=request.POST.get("sel_category")),
                                  family=tbl_family.objects.get(id=id),
                                  member=tbl_teammember.objects.get(id=request.session["mid"]),
                                  product_image=request.FILES.get("pimage"),
                                       )
        return redirect("Webteammember:viewproduct")
    else:
        return render(request,"Teammember/Add_Products.html",{'data':category})    
    

def viewproduct(request):

    data=tbl_product.objects.filter(member=tbl_teammember.objects.get(id=request.session["mid"]))
    prodata = []
    for product in data:
        total_stock = tbl_stock.objects.filter(product=product).aggregate(total=Sum('stock_qty'))['total']
        total_cart = tbl_cart.objects.filter(product=product.id,cart_status=1).aggregate(total=Sum('cart_qty'))['total']
        print(total_stock,"stock")
        print(total_cart,"cart")
        if total_stock is None:
            total_stock = 0
        if total_cart is None:
            total_cart = 0
        if isinstance(total_stock, int):
            total_stock = total_stock
        else:
            total_stock = 0     
            if isinstance(total_cart, int):
                total_cart = total_cart
            else:
                total_cart = 0
        total=  total_stock-total_cart
        print(total)
        product.total_stock = total
        # print(product.total_stock)
    return render(request,"Teammember/ViewProducts.html",{"data":data})

def getStock(id):
    product = tbl_product.objects.get(id=id)
    total_quantity = tbl_cart.objects.filter(product=product, cart_status=1).aggregate(total_quantity=Sum('cart_qty'))['total_quantity']
    if total_quantity is None:
        total_quantity = 0
    return int(total_quantity)  # Convert to integer before returning

def ViewPurchase(request):
    myprofile=tbl_teammember.objects.get(id=request.session["mid"] )
    # booking=tbl_booking.objects.filter(user=myprofile,booking_status__gte=0)
    cartdata=tbl_cart.objects.filter(product__member=myprofile,booking__booking_status__gte=0)
    return render(request,"Teammember/ViewPurchase.html",{'data':cartdata})  

def stock(request,id):
    data=tbl_product.objects.get(id=id)
    if request.method=="POST":
        tbl_stock.objects.create(product=tbl_product.objects.get(id=id),stock_qty=request.POST.get("txtstock"))
        return redirect("Webteammember:viewproduct")
    else:
        return render(request,"Teammember/Stock.html",{"data":data})


def needs(request,id):
    donation=tbl_donationtype.objects.all()
    needs=tbl_familyneedlist.objects.filter(family=tbl_family.objects.get(id=id))
    if request.method=="POST":
        tbl_familyneedlist.objects.create(family=tbl_family.objects.get(id=id),
                                          need=request.POST.get("txtneeds"),
                                          donationtype=tbl_donationtype.objects.get(id=request.POST.get("sel_donation")),
                                          )
        return redirect("Webteammember:family")
    else:
        return render(request,"Teammember/Needlist.html",{"data":donation,"donation":needs})
    
def editneeds(request,id):
    donation=tbl_familyneedlist.objects.get(id=id)
    data=tbl_donationtype.objects.all()
    if request.method=="POST":
        donation.need=request.POST.get("txtneeds")
        donation.donationtype=tbl_donationtype.objects.get(id=request.POST.get("sel_donation"))
        donation.save()
        return redirect("Webteammember:family")
    else:
        return render(request,"Teammember/Needlist.html",{"edit":donation,"data":data})
    
def delneed(request,id):
    donation=tbl_familyneedlist.objects.get(id=id)
    donation.delete()
    return redirect("Webteammember:family")


def logout(request):
    del request.session['mid']
    return redirect("Webguest:login")