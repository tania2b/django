from django.http import JsonResponse
from django.views import View
from todo.models.project import Project


class ProjectListJsonView(View):
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        result = Project.objects.all()
        return JsonResponse([a.title for a in result], safe=False)