from django.db import models

# Create your models here.
class TimeStampModel(models.Model):
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True

class Category(TimeStampModel):
    name = models.CharField(max_length=250,verbose_name="nomi")
    place = models.TextField(blank=True,null=True,verbose_name="joyi")
    
    class Meta:
        verbose_name_plural="Kategoriyalar"
        verbose_name="Kategoriya "

    def __str__(self) -> str:
        return self.name

class Book(TimeStampModel):
    image = models.FileField(upload_to="%d_%m_%Y/",verbose_name="rasm")
    name = models.CharField(max_length=250,verbose_name="nomi")
    category = models.ForeignKey(
        Category,
        related_name='books',
        on_delete=models.CASCADE,
        verbose_name="kategoriya"
    )
    place = models.TextField(blank=True,null=True,verbose_name="joyi")
    amount = models.IntegerField(default=1,verbose_name="miqdor")
    rent_price = models.FloatField(default=0,verbose_name="ijara narxi")
    isbn = models.TextField(unique=True,verbose_name="isbn raqami")

    class Meta:
        verbose_name_plural="Kitoblar"
        verbose_name="Kitob "
        ordering=["-id"]

    def __str__(self) -> str:
        return self.name
    
class Customer(TimeStampModel):
    first_name = models.CharField(max_length=250,verbose_name="ismi")
    last_name = models.CharField(max_length=250,verbose_name="familiyasi")
    location = models.TextField(verbose_name="manzili")
    id_card = models.TextField(verbose_name="passport seriasi")

    class Meta:
        verbose_name_plural="Mijozlar"
        verbose_name="Mijoz "

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

class Rent(TimeStampModel):
    book = models.ForeignKey(
        Book,
        related_name="rents",
        on_delete=models.CASCADE,
        verbose_name="kitob"
    )
    customer = models.ForeignKey(
        Customer,
        related_name="rents",
        on_delete=models.CASCADE,
        verbose_name="mijoz"
    )
    amount = models.IntegerField(default=1,verbose_name="miqdor")
    return_time = models.DateTimeField(verbose_name="qaytarish sanasi")

    class Meta:
        verbose_name_plural="Ijaralar"
        verbose_name="Ijara "

    def __str__(self) -> str:
        return f"{self.customer.first_name}-{self.book.name}-{self.return_time}"
