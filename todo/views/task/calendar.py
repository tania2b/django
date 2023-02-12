from django.views.generic import TemplateView
from todo.models.task import Task


class CalendarView(TemplateView):
    model = Task
    template_name = 'tasks_calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.all().values('title', 'due_date', 'pk')
        return context

