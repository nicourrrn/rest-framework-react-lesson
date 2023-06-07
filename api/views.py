
from rest_framework import mixins, generics

from api.models import Project
from api.serializers import ProjectSerializser


class ProjectList(mixins.ListModelMixin, mixins.CreateModelMixin,
                  generics.GenericAPIView):

    queryset = Project.objects.all()
    serializer_class = ProjectSerializser

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)



class ProjectDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin, generics.GenericAPIView):

    queryset = Project.objects.all()
    serializer_class = ProjectSerializser

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
