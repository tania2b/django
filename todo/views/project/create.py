from django.urls import reverse_lazy
from django.views.generic import CreateView
from todo.models.project import Project


class ProjectCreateView(CreateView):
    template_name = 'project_create_view.html'
    model = Project
    fields = ['title', 'description']
    success_url = reverse_lazy('project_list')


