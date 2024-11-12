from django.db import models

class Sala(models.Model):
    nome = models.CharField(max_length=100)

class Professor(models.Model):
    sala = models.ForeignKey(Sala, related_name='professores', on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    materia = models.CharField(max_length=100)

class Aluno(models.Model):
    sala = models.ForeignKey(Sala, related_name='alunos', on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=20)
    data_adicionado = models.DateField(auto_now_add=True)
