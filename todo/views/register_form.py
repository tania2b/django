from django.contrib.auth.models import User
from django.urls import reverse
from django.views import generic
from django.contrib import messages
from todo.forms.register import RegisterForm
"""from todo.models import user
from todo.models.user import UserProfile"""


class RegisterFormView(generic.FormView):
    template_name = 'register_form.html'
    form_class = RegisterForm

    def form_valid(self, form):
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        # profile_picture = form.cleaned_data['profile_picture']
        try:
            User.objects.create_user(
                username=username, email=email, password=password
            )
            # user_profile = UserProfile.objects.create(user=user, profile_picture=profile_picture)
            return super().form_valid(form)
            messages.add_message(self.request, messages.INFO, 'User created successfully !')
        except Exception as e:
            form.add_error(None, 'Unexpected error !')
            return super().form_invalid(form)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('login')
