from django.shortcuts import render
from django.http import HttpResponse
from .models import PassengerClass
from .serializers import PassengerSerializer
from django.http import JsonResponse
from rest_framework.renderers import JSONRenderer
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def api_request(request):
    if request.method == 'GET':
        data = request.body
        stream = io.BytesIO(data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        if id is not None:
            obj = PassengerClass.objects.get(id=id)
            serial = PassengerSerializer(obj)
            json_data = JSONRenderer().render(serial.data)
            return HttpResponse(json_data, content_type='application/json')
        obj = PassengerClass.objects.all()
        serial = PassengerSerializer(obj, many=True)
        json_data = JSONRenderer().render(serial.data)
        return HttpResponse(json_data, content_type='application/json')
    elif request.method == 'POST':
        data = request.body
        stream = io.BytesIO(data)
        pythondata = JSONParser().parse(stream)
        serial = PassengerSerializer(data=pythondata)
        if serial.is_valid():
            serial.save()
            res = {'msg':'User Created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
    elif request.method == 'PUT':
        data = request.body
        stream = io.BytesIO(data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        obj = PassengerClass.objects.get(id=id)
        serial = PassengerSerializer(obj, data=pythondata, partial=True)
        if serial.is_valid():
            serial.save()
            res = {'msg':'User Updated'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
    elif request.method == 'DELETE':
        data = request.body
        stream = io.BytesIO(data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        obj = PassengerClass.objects.get(id=id)
        obj.delete()
        res = {'msg':'User Delete'}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data, content_type='application/json')
