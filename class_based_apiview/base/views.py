from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *

# Create your views here.
## CRUD function
class studentapi(APIView):
    def get(self, request, format= None, pk= None):
        id=pk
        if id is not None:
            stu = Student.objects.get(id=pk)
            serializer= StudentSerializer(stu)
            return Response(serializer.data)
        stu= Student.objects.all()
        serializer= StudentSerializer(stu, many=True)
        return Response(serializer.data)
    
    def post(self, request, format= None):
        serializer= StudentSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'})
        return Response(serializer.errors)
    
    def put(self, request, format= None, pk= None):
        stu= Student.objects.get(id = pk)
        serializer= StudentSerializer(stu, data= request.data ,partial= True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Updated'})
        return Response(serializer.errors)
    
    def delete(self, request, format= None, pk= None):
        stu= Student.objects.get(id = pk)
        stu.delete()
        return Response({'msg':'Data Deleted'})

        
