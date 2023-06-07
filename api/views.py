
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse, HttpRequest
from rest_framework.parsers import JSONParser
from api.models import Project
from api.serializers import ProjectSerializser

@csrf_exempt
def project_list(request: HttpRequest):
    if request.method == 'GET':
        projects = Project.objects.all()
        serializer = ProjectSerializser(projects, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProjectSerializser(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ProjectSerializser(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    return HttpResponse(status=404)

@csrf_exempt 
def project_detail(request: HttpRequest, pk: int):
    try: 
        proj = Project.objects.get(pk=pk)
    except Project.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ProjectSerializser(proj)
        return JsonResponse(serializer.data)

    elif request.method == "DELETE":
        proj.delete()
        return HttpResponse(status=204)

    return HttpResponse(status=404)
