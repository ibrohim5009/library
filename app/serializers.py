from rest_framework import serializers
from .models import Category, Kitob, Customer, Rent

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class KitobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kitob
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class RentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rent
        fields = '__all__'
