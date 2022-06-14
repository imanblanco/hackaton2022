from django.shortcuts import render
from rest_framework import viewsets

from .models import Order
from .serializers import OrderSerializers
from rest_framework .permissions import IsAuthenticated


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializers
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        return {'request' : self.request}
