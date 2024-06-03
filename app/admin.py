from django.contrib import admin
from .models import Category,Book,Rent,Customer
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display=["id","name","created_date","updated_date"]
    list_display_links=["id","name",]
    list_filter=["id","name",]
    search_fields=["name"]

admin.site.register(Category,CategoryAdmin)
admin.site.register(Book)
admin.site.register(Rent)
admin.site.register(Customer)