from django.db import models

# Create your models here.


class reg(models.Model):
    First_name = models.CharField(max_length=30)
    Last_name = models.CharField(max_length=30)
    Birth_date = models.DateField()
    Age = models.PositiveIntegerField()
    Password = models.CharField(max_length=50)
    Confirm_password = models.CharField(max_length=50)

# -----------------------------------------------------------------------
class Login(models.Model):
    Username = models.CharField(max_length=100)
    Password = models.CharField(max_length=50)
    
# -----------------------------------------------------------------------

class person(models.Model):
    F_Name=models.CharField(max_length=30)
    L_name=models.CharField(max_length=30)

# ----------------------------------------------------------------------- 


class Author(models.Model):
    Name = models.CharField(max_length=100)
    Desc = models.TextField(max_length=300)


class Book(models.Model):
    Title = models.CharField(max_length=100)
    Desc = models.TextField(max_length=300)
    Author = models.ManyToManyField(Author)
    
# -----------------------------------------------------------------------

class Vehicle(models.Model):
    Reg_No = models.IntegerField()
    Owner  = models.CharField(max_length=100)

class Car(models.Model):
    Vehicle = models.OneToOneField(Vehicle,on_delete= models.CASCADE,primary_key=True)
    Car_Model = models.CharField(max_length=100)
    
# -----------------------------------------------------------------------
    
class Musician(models.Model):
    F_Name = models.CharField(max_length=50)
    L_Name = models.CharField(max_length=50)
    Instrument = models.CharField(max_length=100)

class Album(models.Model):
    Title = models.CharField(max_length=100)
    Artist = models.ForeignKey(Musician,on_delete=models.CASCADE)
    Release_Date = models.DateField()
    Num_Stars = models.IntegerField()

class Song(models.Model):
    Album = models.ForeignKey(Album,on_delete=models.CASCADE)
    
# -----------------------------------------------------------------------
    
class Runner(models.Model):
    MedalType = models.TextChoices('MedalType','GLOD SILVER BRONZE')
    Name = models.CharField(max_length=60)
    Medal = models.CharField(blank=True,choices=MedalType.choices,max_length=10)
    
# -----------------------------------------------------------------------
    
class Fruit(models.Model):
    Name = models.CharField(max_length=100,primary_key=True)
    
# -----------------------------------------------------------------------

class Place(models.Model):
    Name = models.CharField(max_length=50)
    Address = models.CharField(max_length=80)

class Restaurant(Place):
    Serves_Hot_Dogs = models.BooleanField(default=False)
    Serves_Pizza = models.BooleanField(default=False)

# -----------------------------------------------------------------------
    
class Item(models.Model):
    Name = models.CharField(max_length=128)
    Price = models.DecimalField(max_digits= 5,decimal_places=2)
    
    def __str__(self):
        return self.Name

class Customer(models.Model):
    Name = models.CharField(max_length=128)
    Age = models.IntegerField()
    Iteam_Purchased = models.ManyToManyField(Item,through = 'Purchase')
    
    def __str__(self):
        return self.Name
    
class Purchase(models.Model):
    Item = models.ForeignKey(Item,on_delete=models.CASCADE)
    Customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    Date_Purchased = models.DateField()
    Quantity_Purchased = models.IntegerField()    

# -----------------------------------------------------------------------
    
class Blog(models.Model):
    Name = models.CharField(max_length=100)
    Tagline = models.TextField()
    
# -----------------------------------------------------------------------
class CommonInfo(models.Model):
    Name = models.CharField(max_length=100)
    Age = models.PositiveIntegerField()

# ----------------------------------------------------------------------- 
    
class Group(models.Model):
    Group_Name = models.CharField(max_length=50)
    Created_At = models.DateField(auto_now_add=True) 
    Updated_At = models.DateField(auto_now=True)
    Providers = models.ManyToManyField('Provider',through='Grouplocations') 
    
class Provider(models.Model):
    First_Name = models.CharField(max_length=50)
    Created_AT = models.DateField(auto_now_add=True)
    Updated_At = models.DateField(auto_now=True)    

class GroupLocations(models.Model):
    Provider = models.ForeignKey('Provider',on_delete=models.CASCADE)
    Group = models.ForeignKey('Group',on_delete=models.SET_NULL,null=True)
    Address = models.CharField("Address line",max_length=1024)
    Doing_Business_As = models.CharField(max_length= 255)
    Created_AT = models.DateField(auto_now_add=True)
    updated_At = models.DateField(auto_now=True)
  
    