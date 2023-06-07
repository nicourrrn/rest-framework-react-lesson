
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

from api.models import Project
from api.serializers import ProjectSerializser

@api_view(["GET", "PUT"])
def project_list(request: Request, format=None):
    if request.method == "GET":
        projects = Project.objects.all()
        serialized = ProjectSerializser(projects, many=True)
        return Response(serialized.data)
    elif request.method == "PUT":
        serialized = ProjectSerializser(data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=status.HTTP_201_CREATED)
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "DELETE"])
def project_detail(request: Request, pk: int, format=None):
    try:
        proj = Project.objects.get(pk=pk)
    except Project.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    match request.method:
        case "GET":
            serialized = ProjectSerializser(proj)
            return Response(serialized.data)
        case "DELETE":
            proj.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
