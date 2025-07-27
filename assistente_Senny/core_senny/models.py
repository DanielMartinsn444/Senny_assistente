from django.db import models
from django.contrib.auth.models import User


class Cadastro(models.Model):
    usuario= models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    telefone= models.CharField(
        max_length= 15,
        blank=True,
        null=True,
        help_text= "Número de telefone com DDD (Ex: 5511987654321)"
    )
    
    def __str__(self):
        return f"perfil de {self.usuario.username}"
    
    class Meta:
        verbose_name= 'Perfil do Usuário'
        verbose_name_plural= 'Perfis dos Usuários'
    