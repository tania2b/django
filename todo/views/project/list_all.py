from django.views.generic import ListView
from todo.models.project import Project


class ProjectListViewAll(ListView):
    template_name = 'project_list_view_all.html'
    model = Project
