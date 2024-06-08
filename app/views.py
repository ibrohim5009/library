from .models import Category, Book, Customer, Rent
from .serializers import CategorySerializer, BookSerializer, CustomerSerializer, RentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework import status

class CategoryQuerySetApiView(APIView):
    def get(self,request,*args,**kwargs):
        queryset=Category.objects.all()
        serializer=CategorySerializer(queryset,many=True)
        return Response(serializer.data)
    
    def post(self,request,*args,**kwargs):
        print(request.data)
        data=request.data
        # obj1=Category(name=data["name"],place=data["place"])
        # obj1.save()
        # obj1=Category.objects.create(name=data["name"],place=data["place"])
        obj1=Category.objects.get_or_create(name=data["name"],place=data["place"])
        print(obj1)
        return Response({})

class CategoryDetailApiView(A`PIView):
    def get(self,request,pk,*args,**kwargs):
        instance=get_object_or_404(Category,pk=pk)
        serializer=CategorySerializer(instance)
        return Response(serializer.data)
    
    def delete(self,request,pk,*args,**kwargs):
        return Response({})

# Steps viewset
# 1-query-set get   
# 2-query-set post
# 3-detail delete
# 4-detail get

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
        query=request.GET.get("query","")
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

