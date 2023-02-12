from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DeleteView
from todo.models.task import Task


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'task_confirm_delete_view.html'
    model = Task
    success_url = 'my_project_list'



