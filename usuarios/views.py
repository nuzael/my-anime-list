from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView, ListView
from .forms import UsuarioForm

# TemplateView
class IndexTemplate(TemplateView):
    template_name = 'usuarios/index.html'

# CreateView
class UsuarioCreate(CreateView):
    form_class = UsuarioForm
    template_name = 'usuarios/cadastro.html'
    success_url = reverse_lazy('todos-animes')

# ListView
class DashboardList(LoginRequiredMixin, ListView):
    model = User
    fields = ['first_name', 'username', 'password']
    template_name = 'usuarios/dashboard.html'