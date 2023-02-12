from django.views.generic import ListView
from todo.models.task import Task
import datetime


class TaskListView(ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'object_list'

    def get_queryset(self):
        today = datetime.datetime.now().date()
        return Task.objects.filter(due_date=today)
