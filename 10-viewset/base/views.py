from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import viewsets

class StudentViewSet(viewsets.ViewSet):
    def list(self, request):
        stu= Student.objects.all()
        serializer= StudentSerializer(stu, many= True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk= None):
        if pk is not None:
            stu= Student.objects.get(pk=pk)
            serializer= StudentSerializer(stu)
            return Response(serializer.data)
        
    def create(self, request):
        serializer= StudentSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Created'})
        return Response(serializer.errors)
    
    def update(self, request, pk= None):
        id= pk
        stu= Student.objects.get(pk=id)
        serializer= StudentSerializer(stu, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Complete Data Updates'})
        return Response(serializer.errors)
    
    def delete(self, request, pk):
        id= pk
        stu= Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg': 'Data Deleted'})


