from django.urls import reverse
from django.views.generic import UpdateView
from todo.models.task import Task


class TaskUpdateView(UpdateView):
    template_name = 'task_update_view.html'
    model = Task
    fields = ['title', 'due_date', 'complete', 'assigned_to']
    success_url = 'projects/list'

    def get_success_url(self):
        return reverse('project_list')

