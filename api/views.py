from django.http import Http404

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView

from api.models import Project
from api.serializers import ProjectSerializser

class ProjectList(APIView):

    def get(self, request: Request, format=None):
        projects = Project.objects.all()
        serialized = ProjectSerializser(projects, many=True)
        return Response(serialized.data)

    def post(self, request: Request, format=None):
        serialized = ProjectSerializser(data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=status.HTTP_201_CREATED)
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

class ProjectDetail(APIView):

    def get_object(self, pk: int) -> Project:
        try:
            return Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            raise Http404

    def get(self, request: Request, pk: int, format=None):
        project = self.get_object(pk)
        serialized = ProjectSerializser(project)
        return Response(serialized.data)

    def post(self, request: Request, pk:int, format=None):
        project = self.get_object(pk)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

