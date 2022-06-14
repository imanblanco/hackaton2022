from django.shortcuts import render
from .models import Category
from .serializers import CategorySerializers
from rest_framework import generics


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
# Create your views here.
