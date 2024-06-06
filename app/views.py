from rest_framework import viewsets
from .models import Category, Book, Customer, Rent
from .serializers import CategorySerializer, BookSerializer, CustomerSerializer, RentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class RentViewSet(viewsets.ModelViewSet):
    queryset = Rent.objects.all()
    serializer_class = RentSerializer

class EmptyDataView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({"data": []}, status=status.HTTP_200_OK)
class EmptyPostDataView(APIView):
    def get(self, request, *args, **kwargs):
        return Response(status=status.HTTP_201_CREATED)