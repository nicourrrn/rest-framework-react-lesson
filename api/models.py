from django.db.models import Model, CharField, \
    TextField, ForeignKey, fields_all 
from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.proxy import fields

from rest_framework.serializers import ModelSerializer ,HyperlinkedModelSerializer, Serializer
from rest_framework import serializers 

class Project(Model):
    created = models.DateTimeField(auto_now_add=True)
    title = CharField(max_length=64)

    class Meta:
        ordering = ['created']

