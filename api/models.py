from django.db.models import Model, CharField, ForeignKey 
from django.db import models

class Project(Model):
    created = models.DateTimeField(auto_now_add=True)
    title = CharField(max_length=64)
    owner = ForeignKey('auth.User', related_name="projects", on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']

