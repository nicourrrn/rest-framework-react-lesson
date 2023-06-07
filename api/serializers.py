from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField

from api.models import Project


class ProjectSerializser(ModelSerializer):
    class Meta: 
        model = Project
        fields = ['id', 'title']

class UserSerrializer(ModelSerializer):
    projects = PrimaryKeyRelatedField(many=True, queryset=Project.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'projects']
