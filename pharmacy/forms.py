from django import forms
from .models import *


class Doctor(forms.ModelForm):
    class Meta:
        model= Doctor
        fields= ["doctor_ssn", "doctor_name", "experience", "specilization"]

class DateInput(forms.DateInput):
    input_type = 'date'

class Drugs(forms.ModelForm):
    class Meta:
        model= Drugs
        fields= ["drug_id", "drugname", "category", "price","manufacturing_date" ,"expiry_date"] 
        widgets = {
            'expiry_date': DateInput(),
            'manufacturing_date': DateInput(),
        }
        
              

class Usert(forms.ModelForm):
    class Meta:
        model=  Usert
        fields= ["login", "user_ssn","username","email","phone" ,"gender","role"] 

class Patient(forms.ModelForm):
    class Meta:
        model= Patient
        fields= ["patient_ssn", "gender","patient_name","patient_address","patient_phonenumber"]                 

class Manufacturer(forms.ModelForm):
    class Meta:
        model= Manufacturer
        fields= ["m_id", "manufacturer_name"]

class Stock(forms.ModelForm):
    class Meta:
        model= Stock
        fields= ["stock_id", "tyype","stocknumber","sdescription","no_items","drug"]


class Supplier(forms.ModelForm):
    class Meta:
        model=  Supplier
        fields= ["supplier_id", "supplier_name","supplier_type"]

class PrescribeSell(forms.ModelForm):
    class Meta:
        model= PrescribeSell
        fields= ["patient_ssn", "doctor_ssn","drug","quantity","date","bill"]        


    
class StockSupplier(forms.ModelForm):
    class Meta:
        model= StockSupplier
        fields= ["stock", "supplier"]

class Manufactures(forms.ModelForm):
    class Meta:
        model= Manufactures
        fields= ["drug_id", "m_id"]        


