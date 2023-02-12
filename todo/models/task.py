from django.db import models
from django.contrib.auth.models import User
from todo.models.project import Project


class Task(models.Model):
    title = models.CharField(max_length=200)
    due_date = models.DateField()
    complete = models.BooleanField(default=False)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    project = models.ManyToManyField(Project, blank=True)

    def __str__(self):
        return f"{self.id} - {self.title}"

"""
    def progress_percentage(self):
        user_tasks = Task.objects.filter(assigned_to=self.request.user, project=self.project)
        total_tasks = user_tasks.count()
        completed_tasks = user_tasks.filter(complete=True).count()
        return round(100 * completed_tasks / total_tasks) if total_tasks > 0 else 0
"""