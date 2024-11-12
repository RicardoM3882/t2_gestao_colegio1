from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DeleteView, DetailView
from .models import Sala, Professor, Aluno

# View para criar uma nova sala
class SalaCreateView(CreateView):
    model = Sala
    fields = ['nome']
    template_name = 'salas/sala_form.html'
    success_url = reverse_lazy('sala-list')

# View para listar todas as salas
class SalaListView(ListView):
    model = Sala
    template_name = 'salas/sala_list.html'
    context_object_name = 'salas'

# View para exibir detalhes de uma sala específica
class SalaDetailView(DetailView):
    model = Sala
    template_name = 'salas/sala_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['professores'] = self.object.professores.all()
        context['alunos'] = self.object.alunos.all()
        return context

# View para excluir uma sala
class SalaDeleteView(DeleteView):
    model = Sala
    template_name = 'salas/sala_confirm_delete.html'
    success_url = reverse_lazy('sala-list')

# View para adicionar um professor a uma sala específica
class ProfessorCreateView(CreateView):
    model = Professor
    template_name = 'salas/professor_form.html'
    fields = ['nome', 'materia']

    def form_valid(self, form):
        sala = get_object_or_404(Sala, pk=self.kwargs['pk'])
        form.instance.sala = sala
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('sala-detail', args=[self.object.sala.pk])

# View para adicionar um aluno a uma sala específica
class AlunoCreateView(CreateView):
    model = Aluno
    template_name = 'salas/aluno_form.html'
    fields = ['nome', 'matricula']

    def form_valid(self, form):
        sala = get_object_or_404(Sala, pk=self.kwargs['pk'])
        form.instance.sala = sala
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('sala-detail', args=[self.object.sala.pk])

# View para excluir um professor de uma sala
class ProfessorDeleteView(DeleteView):
    model = Professor
    template_name = 'salas/professor_confirm_delete.html'  # Crie um template de confirmação se desejar
    pk_url_kwarg = 'professor_id'
    
    def get_success_url(self):
        # Redireciona para a página de detalhes da sala após a exclusão
        return reverse('sala-detail', kwargs={'pk': self.object.sala.pk})

# View para excluir um aluno de uma sala
class AlunoDeleteView(DeleteView):
    model = Aluno
    template_name = 'salas/aluno_confirm_delete.html'  # Crie um template de confirmação se desejar
    pk_url_kwarg = 'aluno_id'
    
    def get_success_url(self):
        # Redireciona para a página de detalhes da sala após a exclusão
        return reverse('sala-detail', kwargs={'pk': self.object.sala.pk})
