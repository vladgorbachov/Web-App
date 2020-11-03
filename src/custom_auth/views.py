from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView


class UserAccountLoginView(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('profiles:list')


class UserAccountLogoutView(LogoutView):
    template_name = 'login.html'
    success_url = reverse_lazy('profiles:list')
