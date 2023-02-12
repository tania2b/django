from django.urls import reverse_lazy
from django.views.generic import CreateView

from todo.models.project import Project
from todo.models.task import Task


class TaskCreateView(CreateView):
    template_name = 'task_create_view.html'
    model = Task
    fields = ['title', 'due_date', 'assigned_to']

    def form_valid(self, form):
        task = form.save()
        task.project.set([Project.objects.get(id=self.kwargs['project_id'])])
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project_id'] = self.kwargs['project_id']
        return context

    def get_success_url(self):
        return reverse_lazy('project_detail', kwargs={'pk': self.kwargs['project_id']})
