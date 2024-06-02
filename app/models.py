from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField()
    place = models.TextField(auto_created=250)

class Kitob(models.Model):
    image = models.FileField(upload_to="%id_%m_%Y/")
    name = models.CharField(max_length=250)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )
    place = models.TextField(auto_created=250)
    amount = models.BigIntegerField()
    rent_price = models.FloatField()
    ISBN = models.UUIDField()

class Rent(models.Model):
    kitob = models.ForeignKey(
        Kitob,
        on_delete=models.CASCADE
    )
    customer = models.BigIntegerField()
    amount = models.BigIntegerField()
    return_time = models.TimeField()
    
class Customer(models.Model):
    last_name = models.CharField()
    lirst_name = models.CharField()
    location = models.TextField()
    card_number_Seria = models.BigIntegerField()

