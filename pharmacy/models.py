from django.db import models
from django.db.models import Model

# Create your models here.
class Destination(models.Model):
    name=models.CharField(max_length=100)
    img=models.TextField(blank=True , null=True)
    desc=models.TextField()
    price=models.IntegerField()
    sales=models.IntegerField(blank=True , null=True)






class Doctor(models.Model):
    doctor_ssn = models.IntegerField(primary_key=True)
    doctor_name = models.CharField(max_length=30, blank=True, null=True)
    experience = models.IntegerField(db_column='Experience', blank=True, null=True)  # Field name made lowercase.
    specilization = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'doctor'


class Drugs(models.Model):
    drug_id = models.IntegerField(primary_key=True)
    drugname = models.CharField(max_length=40, blank=True, null=True)
    category = models.CharField(max_length=50, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    manufacturing_date = models.DateField(db_column='Manufacturing_date', blank=True, null=True)  # Field name made lowercase.
    expiry_date = models.DateField(db_column='Expiry_date', blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return self.drugname

    class Meta:
        managed = True
        db_table = 'drugs'


class Login(models.Model):
    login_id = models.CharField(primary_key=True, max_length=50)
    username = models.CharField(max_length=40, blank=True, null=True)
    password = models.CharField(max_length=40, blank=True, null=True)
    userrole = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'login'


class Manage(models.Model):
    stock = models.ForeignKey('Stock', models.DO_NOTHING, blank=True, null=True)
    user_ssn = models.ForeignKey('Usert', models.DO_NOTHING, db_column='user_ssn', blank=True, null=True)
    drug = models.ForeignKey(Drugs, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'manage'


class Manufacturer(models.Model):
    m_id = models.IntegerField(primary_key=True)
    manufacturer_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'manufacturer'


class Manufactures(models.Model):
    drug_id = models.ForeignKey(Drugs, models.DO_NOTHING, blank=True, null=True)
    m_id = models.ForeignKey(Manufacturer, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'manufactures'


class Patient(models.Model):
    patient_ssn = models.IntegerField(primary_key=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    patient_name = models.CharField(max_length=20, blank=True, null=True)
    patient_address = models.CharField(max_length=70, blank=True, null=True)
    patient_phonenumber = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'patient'


class PrescribeSell(models.Model):
    patient_ssn = models.ForeignKey(Patient, models.DO_NOTHING, db_column='patient_ssn', blank=True, null=True)
    doctor_ssn = models.ForeignKey(Doctor, models.DO_NOTHING, db_column='doctor_ssn', blank=True, null=True)
    drug = models.ForeignKey(Drugs, models.DO_NOTHING, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    date = models.CharField(max_length=40, blank=True, null=True)
    bill = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prescribe_sell'


class Registeruser(models.Model):
    login_id = models.CharField(primary_key=True, max_length=30)
    first_name = models.CharField(max_length=40, blank=True, null=True)
    username = models.CharField(unique=True, max_length=20, blank=True, null=True)
    password = models.CharField(unique=True, max_length=30, blank=True, null=True)
    role = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'registeruser'


class Stock(models.Model):
    stock_id = models.IntegerField(primary_key=True)
    tyype = models.CharField(max_length=40, blank=True, null=True)
    stocknumber = models.IntegerField(blank=True, null=True)
    sdescription = models.CharField(max_length=50, blank=True, null=True)
    no_items = models.CharField(max_length=20, blank=True, null=True)
    drug = models.ForeignKey(Drugs, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock'
class Supplier(models.Model):
    supplier_id = models.IntegerField(primary_key=True)
    supplier_name = models.CharField(max_length=40, blank=True, null=True)
    supplier_type = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'supplier'


class StockSupplier(models.Model):
    stock = models.ForeignKey(Stock, models.DO_NOTHING, blank=True, null=True)
    supplier = models.ForeignKey(Supplier, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_supplier'




class Usert(models.Model):
    login = models.OneToOneField(Login, models.DO_NOTHING, blank=True, null=True)
    user_ssn = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=40, blank=True, null=True)
    email = models.CharField(max_length=40, blank=True, null=True)
    phone = models.BigIntegerField(blank=True, null=True)
    gender = models.CharField(max_length=20, blank=True, null=True)
    role = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usert'