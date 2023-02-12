from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView
from todo.models.project import Project
from todo.models.user import User


class ProjectDetailView(DetailView):
    template_name = 'project_detail_view.html'
    model = Project

