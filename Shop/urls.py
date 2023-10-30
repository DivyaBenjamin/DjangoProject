from django.urls import path
from Shop import views
app_name="webshop"
urlpatterns = [
    path('Home/',views.home,name="home"),
    path('Products/',views.products,name="products"),
    path('Ajaxproduct/',views.Ajaxproduct,name="Ajaxproduct"),
    path('deleteproduct/<int:pid>',views.deleteproduct,name="deleteproduct"),
    path('updatestock/<int:rid>',views.updatestock,name="updatestock"),
    path('Feedback/',views.feedback,name="feedback"),
    path('Complaint/',views.complaint,name="complaint"),
    path('Viewreply/<int:sid>',views.viewreply,name="viewreply"),
    path('Userorders/',views.userorders,name="userorders"),
    path('Updateorder/<int:tid>',views.updateorder,name="updateorder"),
    path('updatereject/<int:uid>',views.updatereject,name="updatereject"),
    path('Report/',views.report,name="report"),
    path('Bookingreport/',views.bookingreport,name="bookingreport"),
    path('Ajaxfromdatereport/',views.Ajaxfromdatereport,name="Ajaxfromdatereport"),
    path('Viewrating/',views.viewrating,name="viewrating"),
    path('Ajaxviewproduct',views.Ajaxviewproduct,name="Ajaxviewproduct"),
]