from django.test import TestCase
from django.shortcuts import resolve_url as r

class HomeTest(TestCase):
    def setUp(self):
        # client ja vem no django, ferramenta base que simula o que o navegar vai enviar para o django
        self.response = self.client.get(r('home'))

    def test_get(self):
        """
        GET / must return status code 200
        """
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """
        must use index.html
        """
        self.assertTemplateUsed(self.response, 'index.html')

    def test_subscription_linl(self):
        """
        must contains 'href="/inscricao/"'
        """
        expected = "href='{}'".format(r('new'))
        self.assertContains(self.response, )

    def test_speakers(self):

        contents = [
            'Grace Hopper','http://hbn.link/hopper-pic','Alan Turing','http://hbn.link/turing-pic'
        ]

        for expected in contents:
            with self.subTest():
                self.assertContains(self.response, expected)


    def test_speakers_link(self):
        expected = 'href="{}#speakers'.format(r('home'))
