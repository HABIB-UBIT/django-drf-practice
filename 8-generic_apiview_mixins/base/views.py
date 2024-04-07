from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin
from .models import *
from .serializers import *

# Create your views here.
## CRUD function using Generic APIView and Mixins

######## SEPERATELY #########

# class studentlist(GenericAPIView,ListModelMixin):
#     queryset= Student.objects.all()
#     serializer_class= StudentSerializer
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

# class studentcreate(GenericAPIView,CreateModelMixin):
#     queryset= Student.objects.all()
#     serializer_class= StudentSerializer
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
    
# class studentretrieve(GenericAPIView,RetrieveModelMixin):
#     queryset= Student.objects.all()
#     serializer_class= StudentSerializer
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
    
# class studentupdate(GenericAPIView,UpdateModelMixin):
#     queryset= Student.objects.all()
#     serializer_class= StudentSerializer
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
    
# class studentdestroy(GenericAPIView,DestroyModelMixin):
#     queryset= Student.objects.all()
#     serializer_class= StudentSerializer
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)



######## COMBINED #########

class studentlistandcreate(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset= Student.objects.all()
    serializer_class= StudentSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
class updatedeleteretrievestudent(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset= Student.objects.all()
    serializer_class= StudentSerializer

    # retrieve
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    # update
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    # destroy
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    

    


