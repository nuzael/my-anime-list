from django.views.generic.edit import CreateView, DeleteView, UpdateView 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.urls import reverse_lazy
from .models import Anime


# ListView
class TodosList(LoginRequiredMixin, ListView):
    model = Anime
    template_name = 'animes/todos_animes.html'

class AssistirList(LoginRequiredMixin, ListView):
    model = Anime
    template_name = 'animes/assistir.html'

class AssistidoList(LoginRequiredMixin, ListView):
    model = Anime
    template_name = 'animes/assistido.html'

class AssistindoList(LoginRequiredMixin, ListView):
    model = Anime
    template_name = 'animes/assistindo.html'

# CreateView
class AnimeCreate(LoginRequiredMixin, CreateView):
    model = Anime
    fields = ['nome', 'temporada', 'status', 'comentarios']
    template_name = 'animes/adicionar.html'
    success_url = reverse_lazy('todos-animes')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

# UpdateView
class AnimeUpdate(LoginRequiredMixin, UpdateView):
    model = Anime
    fields = ['nome', 'temporada', 'status', 'comentarios']
    template_name = 'animes/editar.html'
    success_url = reverse_lazy('todos-animes')

# DeleteView
class AnimeDelete(LoginRequiredMixin, DeleteView):
    model = Anime
    template_name = 'animes/excluir.html'
    success_url = reverse_lazy('todos-animes')