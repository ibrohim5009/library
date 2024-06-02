from django.contrib import admin
from .models import Category,Kitob,Rent,Customer
# Register your models here.

admin.site.register(Category)
admin.site.register(Kitob)
admin.site.register(Rent)
admin.site.register(Customer)