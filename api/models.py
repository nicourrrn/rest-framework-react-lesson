from django.db.models import Model, CharField, ForeignKey 
from django.db import models

class Project(Model):
    created = models.DateTimeField(auto_now_add=True)
    title = CharField(max_length=64)
    owner = ForeignKey('auth.User', related_name="projects", on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']
    
    def __str__(self) -> str:
        return self.title

class Task(Model):
    title = CharField(max_length=64, default='NoNamed')
    project = ForeignKey(Project, related_name='tasks', on_delete=models.CASCADE)
    isDone = models.BooleanField(default=False)

    class Meta:
        ordering = ['isDone']

    def __str__(self) -> str:
        return self.title
