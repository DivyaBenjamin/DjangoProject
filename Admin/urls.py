from django.urls import path
from Admin import views
app_name="webadmin"
urlpatterns = [
    path('District/', views.district,name="district"),
    path('deletedis/<int:did>',views.deletedis,name="deletedis"),
    path('editdistrict/<int:eid>',views.editdistrict,name="editdis"),
    path('Category/',views.category,name="category"),    
    path('deletecat/<int:cid>',views.deletecat,name="deletecat"),
    path('editcategory/<int:fid>',views.editcategory,name="editcat"),
    path('Brand/',views.brand,name="brand"),
    path('deletebrand/<int:bid>',views.deletebrand,name="deletebrand"),
    path('editbrand/<int:gid>',views.editbrand,name="editbrand"),
    path('Place/',views.place,name="place"),
    path('deleteplace/<int:jid>',views.deleteplace,name="deleteplace"),
    path('Subcategory/',views.subcategory,name="subcategory"),
    path('deletesub/<int:hid>',views.deletesub,name="deletesub"),
    path('Newuser/',views.newuser,name="newuser"),
    path('Ajaxplace/',views.Ajaxplace,name="Ajaxplace"),
    path('Shop/',views.shop,name="shop"),
    path('Ajaxshop/',views.Ajaxshop,name="Ajaxshop"),
    path('Viewfeedback/',views.viewfeedback,name="viewfeedback"),
    path('Viewcomplaint/',views.viewcomplaint,name="viewcomplaint"),
    path('Reply/<int:kid>',views.reply,name="reply"),
    path('Viewreport/',views.viewreport,name="viewreport"),
]