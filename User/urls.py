from django.urls import path
from User import views
app_name="Webuser"

urlpatterns = [
    path('homepage/',views.homepage,name="homepage"),
    path('myprofile/',views.MyProfile,name="myprofile"),
    path('editprofile/',views.EditProfile,name="editprofile"),
    path('changepassword/',views.ChangePassword,name="changepassword"),
    path('viewproduct/',views.viewproduct,name="viewproduct"),
    path('addcart/<int:pid>',views.Addcart,name='addcart'),
    path("Mycart/", views.Mycart,name="mycart"),
    path("DelCart/<int:did>", views.DelCart,name="delcart"),
    path("CartQty/", views.CartQty,name="cartqty"),
    path("Pay/", views.Pay,name="pay"),
    path("ViewMyPurchase/",views. ViewMyPurchase,name="ViewMyPurchase"),
    path('Familyneeds/',views.Familyneeds,name="Familyneeds"),
    path('donation/', views.donation,name="donation"),
    path('deldonation/<int:id>', views.deldonation,name="deldonation"),



]