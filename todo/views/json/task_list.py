from django.http import JsonResponse
from django.views import View
from todo.models.task import Task


class TaskListJsonView(View):
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        result = Task.objects.all()
        return JsonResponse([a.title for a in result], safe=False)
