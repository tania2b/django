from django.db import models
from todo.models.tag import Tag


class Project(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True, default='')
    description = models.CharField(max_length=200, null=True, blank=True, default='')
    tags = models.ManyToManyField(Tag, related_name='project')

    def __str__(self):
        return f"{self.id} - {self.title}"

    def get_tasks(self):
        return self.task_set.all()
