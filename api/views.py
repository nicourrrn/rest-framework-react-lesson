from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken, Response 
from rest_framework import  viewsets, request, authentication, request, status


from api.models import Project, Task
from api.serializers import ProjectSerializser, UserSerrializer, TaskSerializers
from api.permissions import IsOwnerOrOreadOnly 

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializser
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsOwnerOrOreadOnly]
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)



class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerrializer


class CustomAuthToken(ObtainAuthToken):

    def post(self, request: request.Request, *args, **kwargs):
        seriazliser = self.serializer_class(data=request.data, 
                                           context={'request': request})
        seriazliser.is_valid()
        user = seriazliser.validated_data['user']
        token, _ = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'username': user.username
        })

class TaskView(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializers
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsOwnerOrOreadOnly]
    
    def perform_create(self, serializer):
        proj = Project.objects.get(pk=self.kwargs.get('projects_pk'))
        print(proj)
        serializer.validated_data['project'] = proj
        return super().perform_create(serializer)


    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(project__id = self.kwargs.get('projects_pk'))
        return queryset

        
    
