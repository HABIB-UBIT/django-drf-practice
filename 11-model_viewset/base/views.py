from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import viewsets

## There are two ViewSets


## Model ViewSet
# class StudentViewSet(viewsets.ModelViewSet):
#     queryset= Student.objects.all()
#     serializer_class= StudentSerializer

## Read-only Model ViewSet
class StudentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset= Student.objects.all()
    serializer_class= StudentSerializer