from rest_framework import serializers
from .models import Category, Book, Customer, Rent

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super(BookSerializer, self).__init__(*args, **kwargs)
        request=self.context.get("request")
        if request and request.method == "GET":
            category=request.GET.get('category')=='true'
            if category:
                self.fields["category"]=CategorySerializer(context=self.context)

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class RentSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super(RentSerializer, self).__init__(*args, **kwargs)
        request = self.context.get("request")
        if request and request.method == "GET":
            book = request.GET.get('book') == 'true'
            if book:
                self.fields["book"] = BookSerializer(context=self.context)
            customer = request.GET.get('customer') == 'true'
            if customer:
                self.fields["customer"] =CustomerSerializer(context=self.context)
                
    class Meta:
        model = Rent
        fields = '__all__'  