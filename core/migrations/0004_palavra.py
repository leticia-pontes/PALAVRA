# Generated by Django 5.0.4 on 2024-05-31 00:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_insere_tema'),
    ]

    operations = [
        migrations.CreateModel(
            name='Palavra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=9)),
                ('dificuldade', models.CharField(choices=[('Fácil', 'Fácil'), ('Médio', 'Médio'), ('Difícil', 'Difícil')], max_length=10)),
                ('tema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.tema')),
            ],
        ),
    ]
