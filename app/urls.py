from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, BookViewSet, CustomerViewSet, RentViewSet

router = DefaultRouter()
router.register("categories", CategoryViewSet)
router.register("books", BookViewSet)
router.register("rents", RentViewSet)
router.register("customers", CustomerViewSet)

urlpatterns=router.urls