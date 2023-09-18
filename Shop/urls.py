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
]