from django.db import migrations, models
import os

def insere_palavras(apps, schema_editor):
    Palavra = apps.get_model('core', 'Palavra')
    Tema = apps.get_model('core', 'Tema')

    default_tema, _ = Tema.objects.get_or_create(descricao='Geral')

    with open('palavras.txt', 'r') as dicionario:
        for palavra in dicionario:
            p = Palavra()
            p.descricao = palavra.strip()
            p.tema_id = default_tema.id
            p.save()

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_palavra'),
    ]

    operations = [
        migrations.RunPython(insere_palavras),
    ]
