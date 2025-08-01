# Generated by Django 5.2.4 on 2025-07-26 23:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="Cadastro",
            fields=[
                (
                    "usuario",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "telefone",
                    models.CharField(
                        blank=True,
                        help_text="Número de telefone com DDD (Ex: 5511987654321)",
                        max_length=15,
                        null=True,
                    ),
                ),
            ],
            options={
                "verbose_name": "Perfil do Usuário",
                "verbose_name_plural": "Perfis dos Usuários",
            },
        ),
    ]
