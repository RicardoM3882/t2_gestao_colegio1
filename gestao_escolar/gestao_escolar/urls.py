"""
URL configuration for gestao_escolar project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from salas import views
from salas.views import SalaListView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.SalaListView.as_view(), name='sala-list'),
    path('sala/add/', views.SalaCreateView.as_view(), name='sala-add'),
    path('sala/<int:pk>/', views.SalaDetailView.as_view(), name='sala-detail'),
    path('sala/<int:pk>/delete/', views.SalaDeleteView.as_view(), name='sala-delete'),
    path('sala/<int:pk>/professor/add/', views.ProfessorCreateView.as_view(), name='professor-add'),
    path('sala/<int:pk>/professor/<int:professor_id>/delete/', views.ProfessorDeleteView.as_view(), name='professor-delete'),
    path('sala/<int:pk>/aluno/add/', views.AlunoCreateView.as_view(), name='aluno-add'),
    path('sala/<int:pk>/aluno/<int:aluno_id>/delete/', views.AlunoDeleteView.as_view(), name='aluno-delete'),
    path('sala/<int:pk>/aluno/<int:aluno_id>/delete/', views.AlunoDeleteView.as_view(), name='aluno-delete'),

]