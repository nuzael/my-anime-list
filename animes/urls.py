from django.urls import path
from .views import TodosList, AssistidoList, AssistindoList, AssistirList, AnimeCreate, AnimeUpdate, AnimeDelete


urlpatterns = [
    path('adicionar/', AnimeCreate.as_view(), name='adicionar'),
    path('editar/<int:pk>', AnimeUpdate.as_view(), name='editar'),
    path('excluir/<int:pk>', AnimeDelete.as_view(), name='excluir'),
    path('todos/', TodosList.as_view(), name='todos-animes'),
    path('assistir/', AssistirList.as_view(), name='assistir'),
    path('assistido/', AssistidoList.as_view(), name='assistido'),
    path('assistindo/', AssistindoList.as_view(), name='assistindo'),
]