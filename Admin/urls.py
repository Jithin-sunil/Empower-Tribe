from django.urls import path
from Admin import views
app_name="Webadmin"

urlpatterns = [
    path('homepage/',views.homepage,name="homepage"),

    path('localbodytype/',views.localbodytype,name="localbodytype"),
    path('editbodytype/<int:id>',views.editbodytype,name="editbodytype"),
    path('delloctype/<int:id>',views.delloctype,name="delloctype"),

    path('localbody/',views.localbody,name="localbody"),
    path('editloc/<int:id>',views.editloc,name="editloc"),
    path('delloc/<int:id>',views.delloc,name="delloc"),

    path('ward/',views.ward,name="ward"),
    path('editward/<int:id>',views.editward,name="editward"),
    path('delward/<int:id>',views.delward,name="delward"),

    path('donation/',views.donation,name="donation"),
    path('editdonationtype/<int:id>',views.editdonationtype,name="editdonationtype"),
    path('deldonationtype/<int:id>',views.deldonationtype,name="deldonationtype"),

    path('team/',views.team,name="team"),
    path('Assign/<int:id>',views.Assign,name="Assign"),
    path('editteam/<int:id>',views.editteam,name="editteam"),
    path('delteam/<int:id>',views.delteam,name="delteam"),

    


    path('category/',views.category,name="category"),
    path('editcat/<int:id>',views.editcat,name="editcat"),
    path('delcat/<int:id>',views.delcat,name="delcat"),

    path('registration/',views.Registration,name="registration"),
    path('delreg/<int:rid>',views.delreg,name="delreg"),

    path('ViewNeeds/',views.ViewNeeds,name="ViewNeeds"),
    path('Accept/<int:did>',views.Accept,name="Accept"),
    path('Reject/<int:did>',views.Reject,name="Reject"),

    path('Acceptedneeds/',views.Acceptedneeds,name="Acceptedneeds"),
    path('Rejectedneeds/',views.Rejectedneeds,name="Rejectedneeds"),

    path('Viewdonation/',views.Viewdonation,name="Viewdonation"),
    path('report/',views.report,name="report"),

    path('viewteammembers/',views.viewteammembers,name="viewteammembers"),
    path('acceptmember/<int:id>',views.acceptmember,name="acceptmember"),
    path('rejectmember/<int:id>',views.rejectmember,name="rejectmember"),




]
