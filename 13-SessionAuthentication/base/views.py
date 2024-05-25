from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly


## Model ViewSet with basic authentication

class StudentViewSet(viewsets.ModelViewSet):
    queryset= Student.objects.all()
    serializer_class= StudentSerializer
    authentication_classes= [SessionAuthentication]
    # permission_classes= [IsAuthenticated]
    # permission_classes= [AllowAny]
    # permission_classes= [IsAdminUser]   ## Only staff status true users can access to the api
    # permission_classes= [IsAuthenticatedOrReadOnly]
    # permission_classes= [DjangoModelPermissions]
    permission_classes= [DjangoModelPermissionsOrAnonReadOnly]
    






## Read-only Model ViewSet
# class StudentViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset= Student.objects.all()
    # serializer_class= StudentSerializer