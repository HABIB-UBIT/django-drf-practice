from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
# Create your views here.

## GET request
# @api_view()  ## By default it is get
# def studentapi(request):
#     return Response({'msg':'Hello World'})

## POST request
# @api_view(['POST'])
# def studentapi(request):
#     if request.method == "POST":
#         print(request.data)
#         return Response({'msg':'This is Post request'})

## Combine request
# @api_view(['Get', 'POST'])
# def studentapi(request):
#     if request.method == "GET":
#         return Response({'msg':'This is Get request'})
#     if request.method == "POST":
#         print(request.data)
#         return Response({'msg':'This is Post request'})


## CRUD function
@api_view(['GET','POST','PUT','DELETE'])
def studentapi(request, pk= None):
    if request.method == "GET":
        # id= request.GET.get('id')
        # id=pk
        if pk is not None:
            stu = Student.objects.get(id=pk)
            serializer= StudentSerializer(stu)
            return Response(serializer.data)
        stu= Student.objects.all()
        serializer= StudentSerializer(stu, many=True)
        return Response(serializer.data)
    
    if request.method == "POST":
        serializer= StudentSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'})
        return Response(serializer.errors)
    
    if request.method == "PUT":
        # id= request.data.get('id')
        stu= Student.objects.get(id = pk)
        serializer= StudentSerializer(stu, data= request.data ,partial= True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Updated'})
        return Response(serializer.errors)
    
    if request.method == "DELETE":
        # id= request.data.get('id')
        stu= Student.objects.get(id = pk)
        stu.delete()
        return Response({'msg':'Data Deleted'})
