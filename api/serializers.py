from django.contrib.auth.models import User
from rest_framework.serializers import HyperlinkedModelSerializer,\
        HyperlinkedRelatedField, ReadOnlyField

from api.models import Project


class ProjectSerializser(HyperlinkedModelSerializer):
    owner = ReadOnlyField(source='owner.username') 

    class Meta: 
        model = Project
        fields = ['url', 'id', 'title', 'owner']

class UserSerrializer(HyperlinkedModelSerializer):
    projects = HyperlinkedRelatedField(many=True, read_only=True,\
            view_name='project-detail')

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'projects']
