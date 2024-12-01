from django.test import TestCase

FACIL = 'FACIL'

class UtilsTest(TestCase):

    def test_get_palavra_aleatoria(self):
        from core.models import Palavra
        from core.utils import get_palavra_aleatoria

        palavras_criadas = list(Palavra.objects.values_list('descricao', flat=True))
        self.assertGreater(len(palavras_criadas), 0)
        
        resultado = get_palavra_aleatoria()
        self.assertIn(resultado, palavras_criadas)