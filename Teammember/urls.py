from django.urls import path
from Teammember import views
app_name="Webteammember"

urlpatterns = [
    path('homepage/',views.homepage,name="homepage"),
    path('myprofile/',views.MyProfile,name="myprofile"),
    path('editprofile/',views.EditProfile,name="editprofile"),
    path('changepassword/',views.ChangePassword,name="changepassword"),
    path('family/',views.family,name="family"),
    path('familymembers/<int:id>',views.familymembers,name="familymembers"),
    path('Product/<int:id>',views.Product,name="Product"),
    path('viewproduct/',views.viewproduct,name="viewproduct"),
    path("ViewPurchase/",views.ViewPurchase,name="ViewPurchase"),
    path("stock/<int:id>",views.stock,name="stock"),
    path("needs/<int:id>",views.needs,name="needs"),
    path("editneeds/<int:id>",views.editneeds,name="editneeds"),
    path("delneed/<int:id>",views.delneed,name="delneed"),
    

    
    
]