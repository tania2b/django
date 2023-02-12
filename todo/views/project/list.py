from django.views.generic import ListView
from django.db.models import Max, ExpressionWrapper, F, FloatField
from todo.models.project import Project
from todo.models.task import Task
from todo.models.tag import Tag


class ProjectListView(ListView):
    template_name = 'project_list_view.html'
    model = Project

    def get_queryset(self):
        queryset = super().get_queryset()
        user_tasks = Task.objects.filter(assigned_to=self.request.user)
        total_tasks = user_tasks.count()
        completed_tasks = user_tasks.filter(complete=True).count()
        self.progress = round(100 * completed_tasks / total_tasks if total_tasks > 0 else 0)

        tags = self.request.GET.getlist('tags')
        if tags:
            queryset = queryset.filter(tags__name__in=tags)

        return queryset.filter(task__assigned_to=self.request.user).annotate(
            max_id=Max('id'),
        ).values('max_id', 'title')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['progress'] = self.progress
        context['tags'] = Tag.objects.all()
        return context

    """
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(task__assigned_to=self.request.user).annotate(
            max_id=Max('id')
        ).values('max_id', 'title')
        
    """