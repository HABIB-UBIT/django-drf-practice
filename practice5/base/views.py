from rest_framework.parsers import JSONParser
import io
from rest_framework.renderers import JSONRenderer
from rest_framework.exceptions import ParseError
from django.http import HttpResponse, JsonResponse
from .models import student
from .serializers import StudentSerializer
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def studentapi(request):
    if request.method == 'GET':
        # Retrieve 'id' from query parameters
        id = request.GET.get('id')

        if id is not None:
            try:
                # Retrieve student by id
                stu = student.objects.get(id=id)
                serializer = StudentSerializer(stu)
                json_data = JSONRenderer().render(serializer.data)
                return HttpResponse(json_data, content_type='application/json')
            except student.DoesNotExist:
                # Handle case where student with given id does not exist
                return HttpResponse("Student not found", status=404)

        # Return all students if 'id' is not provided
        stu = student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')
       

    if request.method == 'POST':
        json_data= request.body
        stream= io.BytesIO(json_data)
        python_data= JSONParser().parse(stream)
        serializer= StudentSerializer(data= python_data)
        if serializer.is_valid():
            serializer.save()
            res= {'msg': 'Data Created'}
            return JsonResponse(res, safe=False)
        json_data= JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type= 'application/json')
    
    if request.method == 'PUT':
        json_data= request.body
        stream= io.BytesIO(json_data)
        python_data= JSONParser().parse(stream)
        id= python_data.get('id')
        stu= student.objects.get(id=id)
        serializer= StudentSerializer(stu, data= python_data, partial= True)  ## Update data partially
        if serializer.is_valid():
            serializer.save()
            res= {'msg':'Data Updated'}
            return JsonResponse(res, safe=False)
        json_data= JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type= 'application/json')
    
    if request.method == 'DELETE':
        json_data= request.body
        stream= io.BytesIO(json_data)
        python_data= JSONParser().parse(stream)
        id= python_data.get('id')
        stu= student.objects.get(id=id)
        stu.delete()
        res= {'msg':'Data Deleted'}
        return JsonResponse(res, safe=False)
        