from django.views.generic import DetailView
from todo.models.task import Task


def TaskDetailView(DetailView):
    template_name = 'task_detail_view.html'
    model = Task


