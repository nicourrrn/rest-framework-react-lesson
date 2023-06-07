from django.contrib.auth.models import User
from rest_framework import generics, permissions, viewsets
from rest_framework.request import Request 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse 

from api.models import Project
from api.serializers import ProjectSerializser, UserSerrializer
from api.permissions import IsOwnerOrOreadOnly 

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializser
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrOreadOnly]
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)



class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerrializer

@api_view(["GET"])
def api_root(request: Request, format=None):
    return Response({
            'users': reverse('user-list', request=request, format=format),
            'projects': reverse('project-list', request=request, format=format)
        })
