from django.shortcuts import render

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter
from .serializers import ProductSerializer
from django.contrib.auth import get_user_model
from .models import Product
from .filters import ProductPriceFilter
from rest_framework import viewsets

User = get_user_model()

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = PageNumberPagination
    filter_backends = [SearchFilter, DjangoFilterBackend]
    filter_class = ProductPriceFilter
    search_fields = ['title', 'description']

    def get_serializer_context(self):
        return {"request": self.request}

class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
