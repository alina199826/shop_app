
from django.urls import reverse
from django.shortcuts import redirect
from django.views.generic import CreateView
from django.contrib.auth import login, get_user_model


class RegisterView(CreateView):
    model = get_user_model()
    template_name = 'create_user.html'


    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.get_success_url())


    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if not next_url:
            next_url = self.request.POST.get('next')
        if not next_url:
            next_url = reverse('index')
        return next_url