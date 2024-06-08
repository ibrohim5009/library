from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (BookViewSet, CategoryQuerySetApiView, CategoryViewSet, CustomerViewSet,
    RentViewSet,CategoryDetailApiView)

router = DefaultRouter()
router.register("categories", CategoryViewSet)
router.register("books", BookViewSet)
router.register("rents", RentViewSet)
router.register("customers", CustomerViewSet)
urlpatterns = [
    path("my-categories/",CategoryQuerySetApiView.as_view()),
    path('my-categories/<int:pk>/', CategoryDetailApiView.as_view()),
]
urlpatterns+=router.urls
