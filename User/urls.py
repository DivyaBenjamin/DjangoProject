from django.urls import path
from User import views
app_name="webuser"
urlpatterns = [
    path('Home/',views.home,name="home"),
    path('Changepassword/',views.changepassword,name="changepassword"),
    path('Editprofile/',views.editprofile,name="editprofile"),
    path('Profile/',views.profile,name="profile"),
    path('Searchshop/',views.searchshop,name="searchshop"),
    path('Ajaxsearch/',views.Ajaxsearch,name="Ajaxsearch"),
    path('Ajaxshopresult/',views.Ajaxshopresult,name="Ajaxshopresult"),
    path('Viewmore/<int:bid>',views.Viewmore,name="Viewmore"),
    path('Viewproducts/',views.viewproducts,name="viewproducts"),
    path('Ajaxcategory/',views.Ajaxcategory,name="Ajaxcategory"),
    path('Ajaxviewproduct/',views.Ajaxviewproduct,name="Ajaxviewproduct"),
    path('Feedback/',views.feedback,name="feedback"),
    path('Complaint/',views.complaint,name="complaint"),
    path('Viewreply/',views.viewreply,name="viewreply"),
    path('Productcart/<int:cid>',views.productcart,name="productcart"),
]