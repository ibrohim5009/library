from rest_framework import viewsets
from .models import Category, Kitob, Customer, Rent
from .serializers import CategorySerializer, KitobSerializer, CustomerSerializer, RentSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class KitobViewSet(viewsets.ModelViewSet):
    queryset = Kitob.objects.all()
    serializer_class = KitobSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class RentViewSet(viewsets.ModelViewSet):
    queryset = Rent.objects.all()
    serializer_class = RentSerializer
