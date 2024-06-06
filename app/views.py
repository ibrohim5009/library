from rest_framework import viewsets
from .models import Category, Book, Customer, Rent
from .serializers import CategorySerializer, BookSerializer, CustomerSerializer, RentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    @action(methods=["GET"],detail=False)
    def search(self,request,*args,**kwargs):
        query=request.GET.get("query")
        queryset = self.filter_queryset(self.get_queryset())
        queryset=queryset.filter(name__icontains=query)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    @action(methods=["GET"],detail=False)
    def search(self,request,*args,**kwargs):
        query=request.GET.get("query")
        queryset = self.filter_queryset(self.get_queryset())
        queryset=queryset.filter(name__icontains=query)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

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