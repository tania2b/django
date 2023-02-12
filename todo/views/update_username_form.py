from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from todo.forms.update_username import UpdateUsernameForm


class UpdateUsernameView(LoginRequiredMixin, generic.FormView):
    template_name = 'update_username.html'
    form_class = UpdateUsernameForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        user = self.request.user
        user.username = form.cleaned_data['username']
        user.save()
        return super().form_valid(form)
