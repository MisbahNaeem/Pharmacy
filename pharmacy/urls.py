from django.urls import path

from . import views

urlpatterns=[
    path('',views.index,name='index'),

    path('index/',views.index,name='index'),

    path('drug/',views.drug,name='drug'),

    path('Drugs/',views.Drugs,name='Drugs'),

    path('patient/',views.patient,name='patient'),

    path('doctor/',views.doctor,name='doctor'),

    path('usert/',views.usert,name='usert'),

    path('supplier/',views.supplier,name='supplier'),

    path('managesupplier/',views.managesupplier,name='managesupplier'),

    path('stock/',views.stock,name='stock'),

    path('sales/',views.sales,name='sales'),

    path('manufacturer/',views.manufacturer,name='manufacturer'),

    path('managemanu/',views.managemanu,name='managemanu'),

    path('login/',views.login,name='login'),

    path("register/",views.register,name="register"),

    path("staff/",views.staff,name="staff"),

    path("admin/",views.admin,name="admin"),

    path("supervisor/",views.supervisor,name="supervisor"),

    path("viewdrugs/",views.viewdrugs,name="viewdrugs"),

    path("viewsales/",views.viewsales,name="viewsales"),

    path("viewstock/",views.viewstock,name="viewstock"),

    path("next/",views.next,name="next"),

    path("viewuser/",views.viewuser,name="viewuser"),

    path("viewexpired/",views.viewexpired,name="viewexpired"),

    path("delete/",views.delete,name="delete"),

    path("manage/",views.manage,name="manage"),

    path("deletedrug",views.deletedrug,name="deletedrug"),

    path("deleteuser",views.deleteuser,name="deleteuser"),

    path("logout/",views.logout,name="logout"),



   

     



]

