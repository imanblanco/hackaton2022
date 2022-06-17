from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

router = DefaultRouter()

router.register('', ProductViewSet)

urlpatterns = []
urlpatterns.extend(router.urls)


# from django.urls import path
# from .views import ProductListView, ProductDetailView
#
#
# urlpatterns = [
#     path('', ProductListView.as_view),
#     path('<int:pk>/', ProductDetailView.as_view),



