from django.contrib import admin
from .models import reg
from .models import Login
from .models import person
from .models import Author
from .models import Book
from .models import Vehicle
from .models import Car
from .models import Musician
from .models import Album
from .models import Song
from .models import Runner
from .models import Fruit
from .models import Place
from .models import Restaurant
from .models import Item
from .models import Customer
from .models import Purchase
from .models import Blog
from .models import CommonInfo
from .models import Group
from .models import Provider
from .models import GroupLocations

# Register your models here.
admin.site.register(reg)
admin.site.register(Login)
admin.site.register(person)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Vehicle)
admin.site.register(Car)
admin.site.register(Musician)
admin.site.register(Album)
admin.site.register(Song)
admin.site.register(Runner)
admin.site.register(Fruit)
admin.site.register(Place)
admin.site.register(Restaurant)
admin.site.register(Item)
admin.site.register(Customer)
admin.site.register(Purchase)
admin.site.register(Blog)
admin.site.register(CommonInfo)
admin.site.register(Group)
admin.site.register(Provider)
admin.site.register(GroupLocations)

# admin.site.register(Membership)
