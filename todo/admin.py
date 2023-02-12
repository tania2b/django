from django.contrib import admin
from todo.models.project import Project
from todo.models.task import Task
from todo.models.tag import Tag
from todo.models.user import UserProfile

# Register your models here.
admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Tag)
admin.site.register(UserProfile)

