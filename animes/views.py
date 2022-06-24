from django.views.generic.edit import CreateView, DeleteView, UpdateView 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from django.urls import reverse_lazy
from .models import Anime


# ListView
class TodosList(LoginRequiredMixin, ListView):
    model = Anime
    paginate_by = 15
    template_name = 'animes/todos_animes.html'

    def get_queryset(self):
        txt_nome = self.request.GET.get('nome')

        if txt_nome:
            self.object_list = Anime.objects.filter(nome__icontains=txt_nome, usuario=self.request.user)
            return self.object_list
        else:
            self.object_list = Anime.objects.filter(usuario=self.request.user)
            return self.object_list

class AssistirList(LoginRequiredMixin, ListView):
    model = Anime
    template_name = 'animes/assistir.html'
    paginate_by = 15

    def get_queryset(self):
        txt_nome = self.request.GET.get('nome')

        if txt_nome:
            self.object_list = Anime.objects.filter(nome__icontains=txt_nome, usuario=self.request.user)
            return self.object_list
        else:
            self.object_list = Anime.objects.filter(usuario=self.request.user, status='Assistir')
            return self.object_list

class AssistidoList(LoginRequiredMixin, ListView):
    model = Anime
    template_name = 'animes/assistido.html'
    paginate_by = 15

    def get_queryset(self):
        txt_nome = self.request.GET.get('nome')

        if txt_nome:
            self.object_list = Anime.objects.filter(nome__icontains=txt_nome, usuario=self.request.user)
            return self.object_list
        else:
            self.object_list = Anime.objects.filter(usuario=self.request.user, status='Assistido')
            return self.object_list

class AssistindoList(LoginRequiredMixin, ListView):
    model = Anime
    template_name = 'animes/assistindo.html'
    paginate_by = 15

    def get_queryset(self):
        txt_nome = self.request.GET.get('nome')

        if txt_nome:
            self.object_list = Anime.objects.filter(nome__icontains=txt_nome, usuario=self.request.user)
            return self.object_list
        else:
            self.object_list = Anime.objects.filter(usuario=self.request.user, status='Assistindo')
            return self.object_list

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

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Anime, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object

# DeleteView
class AnimeDelete(LoginRequiredMixin, DeleteView):
    model = Anime
    fields = '__all__'
    template_name = 'animes/excluir.html'
    success_url = reverse_lazy('todos-animes')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Anime, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object