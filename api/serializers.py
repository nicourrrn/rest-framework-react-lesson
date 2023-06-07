from django.db.models.fields.proxy import fields
from rest_framework.serializers import ModelSerializer
from api.models import Project

class ProjectSerializser(ModelSerializer):
    class Meta: 
        model = Project
        fields = ['id', 'title']
