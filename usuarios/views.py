from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView, ListView

# TemplateView
class IndexTemplate(TemplateView):
    template_name = 'usuarios/index.html'

# CreateView
class UsuarioCreate(CreateView):
    model = User
    fields = ['first_name', 'username', 'password']
    template_name = 'usuarios/cadastro.html'

# ListView
class DashboardList(LoginRequiredMixin, ListView):
    model = User
    fields = ['first_name', 'username', 'password']
    template_name = 'usuarios/dashboard.html'