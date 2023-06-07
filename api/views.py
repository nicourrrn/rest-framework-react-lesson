from django.contrib.auth.models import User
from rest_framework import generics, permissions

from api.models import Project
from api.serializers import ProjectSerializser, UserSerrializer
from api.permissions import IsOwnerOrOreadOnly 

class ProjectList(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializser
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrOreadOnly]
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializser
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrOreadOnly]

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerrializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerrializer
