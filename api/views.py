from django.contrib.auth.models import User
from rest_framework import generics

from api.models import Project
from api.serializers import ProjectSerializser, UserSerrializer

class ProjectList(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializser



class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializser

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerrializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerrializer
