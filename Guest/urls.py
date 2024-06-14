from django.urls import path
from Guest import views
app_name="Webguest"

urlpatterns = [
        path('userreg/',views.UserRegistration,name="userreg"),
        path('login/',views.Login,name="login"),
        path('ViewTeams/',views.ViewTeams,name="ViewTeams"),
        path('MemberRegistration/<int:id>',views.MemberRegistration,name="MemberRegistration"),

]