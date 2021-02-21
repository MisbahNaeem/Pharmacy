from django.shortcuts import render,redirect
from .models import *
from . models import Drugs as dug
from . models import Usert as use
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.db import connection
from django.utils.datastructures import MultiValueDictKeyError
from .forms import *
from .forms import Usert
from django.http import HttpResponse
from django.contrib.auth import logout



#register function
def register (request):  
   if request.method =='POST':
        user=Registeruser()
        user.login_id= request.POST['login_id']
        user.first_name = request.POST['first_name']
        user.username = request.POST['username']
        user.password = request.POST['password']
        user.role = request.POST['role']
        object=Registeruser.objects.all()
        for objects in object:
            if user.username==objects.username:
               messages.info(request,'username taken')
               return render(request,'registeruser.html')     
        user.save()
        return render(request,'login.html')
   else:    
      return render(request,'registeruser.html')

def next (request):
    if request.method =='POST':
        login_id= request.POST.get("login_id")
        role=request.POST.get("role")
        object=Registeruser.objects.all()
        for objects in object:
               if  login_id==objects.login_id and role==objects.role:
                  if role=='staff':
                     return render(request,'staff_menu.html')
                  elif role=='admin':
                     return render(request,'admin_menu.html')
                  elif role=='supervisor':
                     return render(request,'super_menu.html')
    else:
        return render(request,'next.html')

#login view
def login (request):
   if request.method =='POST':
        user=Login()
        out=Registeruser()
        user.login_id= request.POST['login_id']
        user.username = request.POST['username']
        user.password = request.POST['password']
        user.userrole=request.POST['userrole']
        object=Registeruser.objects.all()
        for objects in object:
               if user.username==objects.username and user.login_id==objects.login_id and user.password==objects.password:
                  user.save()
                  if user.userrole=='staff':
                     return render(request,'staff_menu.html')
                  elif user.userrole=='admin':
                     return render(request,'admin_menu.html')
                  elif user.userrole=='supervisor':
                     return render(request,'super_menu.html')
        for objects in object:
               if user.username!=objects.username:
                  messages.info(request,'Invalid Credentails')
                  return render(request,'login.html')         
   else:
      return render(request,'login.html')

def viewdrugs(request):
    cursor = connection.cursor()
    cursor.execute('SELECT * from Drugs')
    rows=cursor.fetchall()
    return render(request,'viewdrugs.html',{'rows':rows})

def viewsales(request):
    cursor = connection.cursor()
    cursor.execute('SELECT drugs.drugname,patient.patient_name,doctor.doctor_name,quantity,price,(quantity*price) as Total_Bill from prescribe_sell,Drugs,patient,Doctor where prescribe_sell.drug_id=Drugs.drug_id and prescribe_sell.patient_ssn=patient.patient_ssn and prescribe_sell.doctor_ssn=Doctor.doctor_ssn')
    rows=cursor.fetchall()
    return render(request,'viewsales.html',{'rows':rows})

   

def viewdoctors(request):
    cursor = connection.cursor()
    cursor.execute('SELECT * from Doctor')
    rows=cursor.fetchall()
    return render(request,'viewdoctor.html',{'rows':rows})

def viewstock(request):
    cursor = connection.cursor()
    cursor.execute('SELECT * from stock')
    rows=cursor.fetchall()
    return render(request,'viewstock.html',{'rows':rows})


def viewexpired(request):
    cursor = connection.cursor()
    cursor.execute('SELECT * from Drugs where expiry_date<=current_date()')
    rows=cursor.fetchall()
    return render(request,'viewexpired.html',{'rows':rows})    

def viewuser(request):
    cursor = connection.cursor()
    cursor.execute('SELECT *  from usert')
    rows=cursor.fetchall()
    return render(request,'viewuser.html',{'rows':rows})

#register  a user 
def admin(request):
   return render(request, 'admin_menu.html')   

def staff(request):
   return render(request, 'Staff_Menu.html') 

def supervisor(request):
   return render(request, 'super_menu.html')        
#adddrug function....
def drug(request):
      form=Drugs(request.POST or None)
      if form.is_valid():
         form.save()
      add={'form':form}    
      return render(request, 'adddrug.html',add)   


def patient(request):
    form=Patient(request.POST or None)
    if form.is_valid():
        form.save()
    context= {'form': form }
    return render(request, 'addpatient.html', context)


def doctor(request):
    form=Doctor(request.POST or None)
    if form.is_valid():
        form.save()
    context= {'form': form }
    return render(request, 'adddoctor.html', context)


        
def manufacturer(request):
    form=Manufacturer(request.POST or None)
    if form.is_valid():
        form.save()
    context= {'form': form }
    return render(request, 'addmanufac.html', context) 
    


def supplier(request):
    form=Supplier(request.POST or None)
    if form.is_valid():
        form.save()
    context= {'form': form }
    return render(request, 'addsupplier.html', context) 


def stock(request):
    form=Stock(request.POST or None)
    if form.is_valid():
        form.save()
    context= {'form': form }
    return render(request, 'addstock.html', context) 

def sales(request):
    form=PrescribeSell(request.POST or None)
    if form.is_valid():
        form.save()
    context= {'form': form }
    return render(request, 'addsales.html', context) 

def managesupplier(request):
      form=StockSupplier(request.POST or None)
      if form.is_valid():
         form.save()
      add={'form':form}    
      return render(request, 'managesupplier.html',add)  

def managemanu(request):
      form=Manufactures(request.POST or None)
      if form.is_valid():
         form.save()
      add={'form':form}    
      return render(request, 'managemanu.html',add)

def usert(request):
    form=Usert(request.POST or None)
    if form.is_valid():
        form.save()
    context= {'form': form }
    return render(request, 'adduser.html', context)

def delete(request):
   return render(request, 'delete.html')    


def deletedrug(request):
      if request.method=="POST":
          drug_id=request.POST.get('drug_id')
          drugname=request.POST.get('drugname')
          object=dug.objects.all()
          out=dug.objects.filter(drug_id=drug_id,drugname=drugname)
          out.delete()     
      return render(request,'Deletedrug.html')


def deleteuser(request):
      if request.method=="POST":
          user_ssn=request.POST.get('user_ssn')
          username=request.POST.get('username')
          object=use.objects.all()
          out=use.objects.filter(user_ssn=user_ssn,username=username)
          out.delete()     
      return render(request,'deleteuser.html')

def manage(request):
   return render(request, 'manage.html')        


      
def logout(request):
    return redirect("/")
    # Redirect to a success page.    


    






      

    
        
   


# Create your views here..
def index(request):
    dest1 = Destination()
    dest1.name= 'Panadol'
    dest1.price='50'
    dest1.img = '1.2.jpg'
    dest1.desc='Panadol Advance 500 mg Tablets are a mild analgesic and antipyretic, and are recommended for the treatment of most painful and febrile conditions, for example, headache including migraine and tension headaches, toothache, backache, rheumatic and muscle pains, dysmenorrhoea, sore throat, and for relieving the fever.'
    dest1.sale=False

    dest2 = Destination()
    dest2.name= 'Lipitor'
    dest2.price='165'
    dest2.img = '2.1.jpg'
    dest2.desc='Lipitor is a prescription medicine used to lower blood levels of “bad” cholesterol (low-density lipoprotein, or LDL), to increase levels of “good” cholesterol (high-density lipoprotein, or HDL), and to lower triglycerides and to treat the symptoms of high cholesterol (hyperlipidemia) and to lower the risk of stroke.'
    dest2.sale=False

    dest3 = Destination()
    dest3.name= 'Amoxicillin'
    dest3.price='100'
    dest3.img = '3.2.jpg'
    dest3.desc='Lipitor is a prescription medicine used to lower blood levels of “bad” cholesterol (low-density lipoprotein, or LDL), to increase levels of “good” cholesterol (high-density lipoprotein, or HDL), and to lower triglycerides and to treat the symptoms of high cholesterol (hyperlipidemia) and to lower the risk of stroke.'
    dest3.sale=False

    dest4 = Destination()
    dest4.name= 'Calpol'
    dest4.price='65'
    dest4.img = '4.1.jpg'
    dest4.desc='CALPOL Infant Suspension is indicated for the treatment of mild to moderate pain and as an antipyretic. It can be used in many conditions including headache, toothache, earache, teething, sore throat, colds & influenza, aches and pains and post-immunisation fever.'
    dest4.sale=False

    dest5 = Destination()
    dest5.name= 'Tramadol'
    dest5.price='45'
    dest5.img = '5.1.png'
    dest5.desc='Tramadol is similar to opioid (narcotic) analgesics. It works in the brain to change how your body feels and responds to pain. Tramadol is a narcotic-like pain relieving oral medicine that is used as a treatment for moderate to severe pain in adults.'
    dest5.sale=False

    dest6 = Destination()
    dest6.name= 'Bioderma'
    dest6.price='80'
    dest6.img = '6.1.jpg'
    dest6.desc='Bioderma Laboratories is a privately owned French pharmaceutical company that specialises in medication for dermatological and hair/scalp conditions, as well as for Pediatry and cell regeneration.'
    dest6.sale=False


    dests =[dest1,dest2,dest3,dest4,dest5,dest6]
    return render(request,'index.html',{'dests':dests})

    

   



