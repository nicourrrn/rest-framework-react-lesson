from django.contrib.auth.models import User, AnonymousUser
from django.core.serializers.json import Serializer
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken, Response 
from rest_framework import  viewsets, request, authentication


from api.models import Project
from api.serializers import ProjectSerializser, UserSerrializer, UserLoginSerializer
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
