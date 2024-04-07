from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView
from .models import *
from .serializers import *

# Create your views here.
## CRUD function using Concrete View Class

######## SEPERATELY #########

# class studentlist(ListAPIView):
#     queryset= Student.objects.all()
#     serializer_class= StudentSerializer

# class studentcreate(CreateAPIView):
#     queryset= Student.objects.all()
#     serializer_class= StudentSerializer

# class studentretrieve(RetrieveAPIView):
#     queryset= Student.objects.all()
#     serializer_class= StudentSerializer

# class studentupdate(UpdateAPIView):
#     queryset= Student.objects.all()
#     serializer_class= StudentSerializer

# class studentdestroy(DestroyAPIView):
#     queryset= Student.objects.all()
#     serializer_class= StudentSerializer
    
######## Combined #########

# class ListCreateStudent(ListCreateAPIView):  ## Works finely for list and create
#     queryset= Student.objects.all()
#     serializer_class= StudentSerializer

# class RetrieveUpdateStudent(RetrieveUpdateAPIView):  ## Works finely for retrieve and update
#     queryset= Student.objects.all()
#     serializer_class= StudentSerializer

# class RetrievedestroyStudent(RetrieveDestroyAPIView):  ## Works finely for retrieve and destroy
#     queryset= Student.objects.all()
#     serializer_class= StudentSerializer

# class RetrieveupdatedestroyStudent(RetrieveUpdateDestroyAPIView):  ## Works finely for retrieve, update and destroy
#     queryset= Student.objects.all()
#     serializer_class= StudentSerializer


######## Most Important and Easy to make CRUD function #########
class ListCreateStudent(ListCreateAPIView):  ## Works finely for list and create
    queryset= Student.objects.all()
    serializer_class= StudentSerializer

class RetrieveUpdateDestroyStudent(RetrieveUpdateDestroyAPIView):  ## Works finely for retrieve, update and destroy
    queryset= Student.objects.all()
    serializer_class= StudentSerializer