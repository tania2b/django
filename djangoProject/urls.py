"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from todo.views.index import IndexView

from todo.views.project.detail import ProjectDetailView
from todo.views.project.list import ProjectListView
from todo.views.project.list_all import ProjectListViewAll
from todo.views.project.create import ProjectCreateView

from todo.views.task.calendar import CalendarView

from todo.views.task.list import TaskListView
from todo.views.task.create import TaskCreateView
from todo.views.task.update import TaskUpdateView
from todo.views.task.delete import TaskDeleteView

from todo.views.register_form import RegisterFormView
from todo.views.login_form import LoginFormView
from todo.views.logout_form import LogoutFormView
from todo.views.update_username_form import UpdateUsernameView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),

    path('task/list', TaskListView.as_view(), name='task_list'),

    path('myprojects/', ProjectListView.as_view(), name='my_project_list'),
    path('projects/', ProjectListViewAll.as_view(), name='project_list'),
    path('projects/create', ProjectCreateView.as_view(), name='project_create'),
    path('projects/detail/<int:pk>', ProjectDetailView.as_view(), name='project_detail'),

    path('projects/<int:project_id>/task/create/', TaskCreateView.as_view(), name='task_create'),
    path('projects/task/update/<int:pk>', TaskUpdateView.as_view(), name='task_update'),
    path('projects/task/delete/<int:pk>', TaskDeleteView.as_view(), name='task_delete'),

    path("calendar/", CalendarView.as_view(), name="task_calendar"),

    path('register', RegisterFormView.as_view(), name='register'),
    path('login', LoginFormView.as_view(), name='login'),
    path('logout', LogoutFormView.as_view(), name='logout'),

    path('password-change/', PasswordChangeView.as_view(), name='password_change'),
    path('password-change/done/', PasswordChangeDoneView.as_view(), name='password_change_done'),

    path('update/username', UpdateUsernameView.as_view(), name='update_username'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
