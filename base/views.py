from django.shortcuts import render
from .models import *
from .forms import *
from .serializers import *
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse

# Create your views here.
def studinfo(request):
    form= studentform()
    if request.method == 'POST':
        form= studentform(request.POST)
        if form.is_valid():
            form.save()
        else:
            pass
    context= {'form':form}
    return render(request, 'base/home.html', context)

def studresp(request,pk):
    stu= Student.objects.get(id = pk)
    serializer= StudentSerializer(stu)
    # json_data= JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data, content_type= 'application/json')

    ## We can also shoe output by Jsonresponse in single line
    return JsonResponse(serializer.data , safe= False)

def studresplist(request):
    stu= Student.objects.all()
    serializer= StudentSerializer(stu, many= True)
    # json_data= JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data, content_type= 'application/json')

    ## We can also shoe output by Jsonresponse in single line
    return JsonResponse(serializer.data , safe= False)
    