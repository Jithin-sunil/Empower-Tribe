from django.shortcuts import render,redirect
from Guest.models import *
from Teammember.models import *
from User.models import *
from django.db.models import Sum
# Create your views here.

def homepage(request):
    return render(request,"User/Homepage.html")


def MyProfile(request): 
    myprofile=tbl_userreg.objects.get(id=request.session["uid"] )
    return render(request,"User/Myprofile.html",{'data':myprofile})

def EditProfile(request): 
    myprofile=tbl_userreg.objects.get(id=request.session["uid"] )
    if request.method=="POST":
        myprofile.member_name=request.POST.get("txtname")
        myprofile.member_email=request.POST.get("txtemail")
        myprofile.member_contact=request.POST.get("txtcontact")
        myprofile.member_address=request.POST.get("txtaddress")
        myprofile.save()
        return redirect("Webuser:myprofile")
    else:
        return render(request,"User/EditProfile.html",{'data':myprofile})

def ChangePassword(request): 
    myprofile=tbl_userreg.objects.get(id=request.session["uid"] )
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
                return render(request,"User/ChangePassword.html",{'msg':msg})   
            else:
                msg="Password mismatch"
                return render(request,"User/ChangePassword.html",{'msg':msg})   
        else:
            msg="Wrong Old Password"
            return render(request,"User/ChangePassword.html",{'msg':msg}) 
    else:
        return render(request,"User/ChangePassword.html") 

def viewproduct(request):
    data=tbl_product.objects.all()

    for product in data:
            total_stock = tbl_stock.objects.filter(product=product).aggregate(total=Sum('stock_qty'))['total']
            total_cart = tbl_cart.objects.filter(product=product.id, cart_status=1).aggregate(total=Sum('cart_qty'))['total']
            print(total_stock, "stock")
            print(total_cart, "cart")
            
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
            
            total =  total_stock - total_cart
            print(total)
            product.total_stock = total


    return render(request,"User/ViewProducts.html",{"data":data, 'product': product})


def getStock(id):
    product = tbl_product.objects.get(id=id)
    total_quantity = tbl_cart.objects.filter(product=product).aggregate(total_quantity=Sum('cart_qty'))['total_quantity']
    if total_quantity is None:
        total_quantity = 0
    return int(total_quantity)

def Addcart(request,pid):
    
        productdata=tbl_product.objects.get(id=pid)
        custdata=tbl_userreg.objects.get(id=request.session["uid"])
        bookingcount=tbl_booking.objects.filter(user=custdata,booking_status=0).count()
        if bookingcount>0:
         bookingdata=tbl_booking.objects.get(user=custdata,booking_status=0)
         cartcount=tbl_cart.objects.filter(booking=bookingdata,product=productdata).count()
         if cartcount>0:
          msg="Already added"
          return render(request,"User/ViewProducts.html",{'msg':msg})
         else:
        
          tbl_cart.objects.create(booking=bookingdata,product=productdata,cart_qty=1)
          msg="Added To cart"
          return render(request,"User/ViewProducts.html",{'msg':msg})
        else:
           tbl_booking.objects.create(user=custdata)
           bookingcount=tbl_booking.objects.filter(booking_status=0,user=custdata).count()
           if bookingcount>0:
            bookingdata=tbl_booking.objects.get(user=custdata,booking_status=0)
            cartcount=tbl_cart.objects.filter(booking=bookingdata,product=productdata).count()
            if cartcount>0:
             msg="Already added"
             return render(request,"User/ViewProducts.html",{'msg':msg})
            else:
             tbl_cart.objects.create(booking=bookingdata,product=productdata,cart_qty=1)
             msg="Added To cart"
            return render(request,"User/ViewProducts.html",{'msg':msg})
    

def Mycart(request):
   if request.method=="POST":
     bookingdata=tbl_booking.objects.get(id=request.session["bookingid"])
     cart = tbl_cart.objects.filter(booking=bookingdata)
     for i in cart:
        i.cart_status = 1
        i.save()
     bookingdata.booking_totalamount=request.POST.get("carttotalamt")
     bookingdata.booking_status=1
     bookingdata.save()
     return redirect("Webuser:pay")
   else:
    customerdata=tbl_userreg.objects.get(id=request.session["uid"])
    bcount=tbl_booking.objects.filter(user=customerdata,booking_status=0).count()
   #cartcount=cart.objects.filter(booking__customer=customerdata,booking__status=0).count()
    if bcount>0:
    #cartdata=cart.objects.filter(booking__customer=customerdata,booking__status=0)
     book=tbl_booking.objects.get(user=customerdata,booking_status=0)
     bid=book.id
     request.session["bookingid"]=bid
     bkid=tbl_booking.objects.get(id=bid)
     cartdata=tbl_cart.objects.filter(booking=bkid)
     data=[]
     for product in cartdata:
        total_stock = tbl_stock.objects.filter(product=product.product).aggregate(total=Sum('stock_qty'))['total']
        total_cart = tbl_cart.objects.filter(product=product.product,cart_status=1).aggregate(total=Sum('cart_qty'))['total']
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
            # print (total)
            # print("stock",total_stock)
            # print("cart",total_cart)
        product.stock = total
        pro_data={
                'id':product.id,
                'product': product,
                'stock':total,
            }
        data.append(pro_data)

        return render(request,"User/MyCart.html",{'pro':pro_data,'data':cartdata})
    else:
      return render(request,"User/MyCart.html")    

def getStock(id):
    product = tbl_product.objects.get(id=id)
    carttotal = tbl_cart.objects.filter(product=product, cart_status=1).aggregate(total_quantity=Sum('cart_qty'))['total_quantity']
    if carttotal is None:
        carttotal = 0
    total_quantity=int(product.product_stock)-int(carttotal)
    return int(total_quantity)

def DelCart(request,did):
   tbl_cart.objects.get(id=did).delete()
   return redirect("Webuser:mycart")

def CartQty(request):
   qty=request.GET.get('QTY')
   cartid=request.GET.get('ALT')
   cartdata=tbl_cart.objects.get(id=cartid)
   cartdata.cart_qty=qty
   cartdata.save()
   return redirect("Webuser:mycart")    

def Pay(request):
   bookingdata=tbl_booking.objects.get(id=request.session["bookingid"])
   amnt=bookingdata.booking_totalamount
   if request.method=="POST":
      bookingdata.payment_status=1
      bookingdata.save()
      return redirect("Webuser:ViewMyPurchase")
   else:
      return render(request,"User/Payment.html",{'amnt':amnt})
   

def ViewMyPurchase(request):
    customerdata=tbl_userreg.objects.get(id=request.session["uid"])
    booking=tbl_booking.objects.filter(user=customerdata,booking_status__gte=0)
    cartdata = []
    for booking_obj in booking:
        carts_for_booking = tbl_cart.objects.filter(booking=booking_obj)
        cartdata.extend(carts_for_booking)
    return render(request,"User/ViewMyPurchase.html",{'data':cartdata})   



def Complaint(request):
    customerdata=tbl_userreg.objects.get(id=request.session["uid"])
    Complaint=tbl_complaint.objects.filter(user=customerdata)
    if request.method=="POST":
       tbl_complaint.objects.create(user=customerdata,
                                    complaint_title=request.POST.get("txttit"),
                                    complaint_content=request.POST.get("txtcomplaint"))
       return redirect("Webuser:Complaint")
    else:
        return render(request,"User/Complaint.html",{'complaint':Complaint}) 

def Delcomplaint(request,did):
    tbl_complaint.objects.get(id=did).delete()
    return redirect("Webuser:Complaint")

def Feedback(request):
    customerdata=tbl_userreg.objects.get(id=request.session["uid"])
    feedback=tbl_feedback.objects.filter(user=customerdata)
    if request.method=="POST":
       tbl_feedback.objects.create(user=customerdata,
                                   feedback_content=request.POST.get("txtpro"))
       return redirect("Webuser:Feedback")
    else:
        return render(request,"User/Feedback.html",{'feedback':feedback})       

def Delfeedback(request,did):
    tbl_feedback.objects.get(id=did).delete()
    return redirect("Webuser:Feedback")   


def Familyneeds(request):
    data=tbl_familyneedlist.objects.filter(need_status=1)
    return render(request,"User/FamilyNeeds.html",{'data':data})

def donation(request):
    don=tbl_donationtype.objects.all()
    user=tbl_userreg.objects.get(id=request.session["uid"])
    data=tbl_donation.objects.filter(user=user)
    if request.method=="POST":
        donation=tbl_donation.objects.create(user=user,donation_type=tbl_donationtype.objects.get(id=request.POST.get("sel_donationtype")),donation_details=request.POST.get("Description"))
        return redirect("Webuser:donation")
    return render(request,"User/Donation.html",{"don":don,"data":data})

def deldonation(request,id):
    tbl_donation.objects.get(id=id).delete()
    return redirect("Webuser:donation")


def logout(request):
    del request.session['uid']
    return redirect("Webguest:login")