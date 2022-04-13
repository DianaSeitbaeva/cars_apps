from django.shortcuts import render
from yaml import serializers
from rest_framework import generics
from .models import Cars
from .serializer import CarsSerializer

class CarsApiView(generics.ListAPIView):
    queryset = Cars.objects.all()
    serialazier_class = CarsSerializer
