from django.core import mail
from django.shortcuts import resolve_url
from django.test import TestCase




class SubscribePostValid(TestCase):
    def setUp(self):
        # client ja vem no django, ferramenta base que simula o que o navegar vai enviar para o django
        data = dict(name='Luiz Arthur', cpf='12345678901', email='luiz@neurondat.com', phone='99-9 9999-9999')
        self.response = self.client.get(resolve_url('new'), data)
        self.email = mail.outbox[0]


    def test_subscription_email_subject(self):

        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):

        expect = 'contato@eventex.com'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):

        expect = ['contato@eventex.com', 'henrique@basctos.net']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):

        contents = ['Luiz Arthur', '12345678907', 'herique@bastos.net', '99-99999-9999']

        for content in contents:
            with self.subTest():
                self.assertEqual(content, self.email.body)


