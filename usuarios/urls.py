from .views import IndexTemplate, UsuarioCreate, DashboardList
from django.contrib.auth import views as auth_views
from django.urls import path


urlpatterns = [
    path('', IndexTemplate.as_view(), name='index'),
    path('cadastro/', UsuarioCreate.as_view(), name='cadastro'),
    path('login/', auth_views.LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='usuarios/index.html'), name='logout'),
    path('dashboard/', DashboardList.as_view(), name='dashboard'),
]