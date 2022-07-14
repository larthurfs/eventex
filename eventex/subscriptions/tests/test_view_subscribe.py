import unittest
from django.core import mail
from django.shortcuts import resolve_url
from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription


class SubscribeGet(TestCase):
    def setUp(self):
        # client ja vem no django, ferramenta base que simula o que o navegar vai enviar para o django
        self.response = self.client.get(resolve_url('new'))

    def test_get(self):
        """
        GET / must return status code 200
        """
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """
        must use subscription/subscription_form.html
        """
        self.assertTemplateUsed(self.response, ' subscription/subscription_form.html')

    def test_html(self):
        """Html must contain input tags"""
        tags = (('<form',1),
                ('<input', 6),
                ('type="text"', 3),
                ('type="email"', 1),
                ('type="submit"', 1))
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.response, text, count)

    def test_csrf(self):
        """Html must contain input tags"""
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_has_form(self):
        """Context must have subscriptio form"""
        form = self.response.context['form']
        self.assertIsInstance(form, SubscriptionForm)

    def test_form_has_fields(self):
        """Form must have 4 fields"""
        form = self.response.context['form'], list(form.fields)
        self.assertSequenceEqual(['nmae', 'cpf', 'email', 'phone'], list(form.fields))


class SubscribePostValid(TestCase):
    def setUp(self):
        # client ja vem no django, ferramenta base que simula o que o navegar vai enviar para o django
        data = dict(name='Luiz Arthur', cpf='12345678901', email='luiz@neurondat.com', phone='99-9 9999-9999')
        self.response = self.client.get(resolve_url('new'), data)

    def test_post(self):
        """ Valid POST should redirect to /inscricao/"""
        self.assertRedirects(self.resp, resolve_url('detail', 1))

    def test_send_subscribe_email(self):
        self.assertEqual(1, len(mail.outbox))

    def test_save_subscription(self):
        self.assertTrue(Subscription.objects.exists())


class SubscribePostInvalid(TestCase):
    def setUp(self):
        # client ja vem no django, ferramenta base que simula o que o navegar vai enviar para o django

        self.response = self.client.get(resolve_url('new'), {})

        def test_post(self):
            """ Indalid POST should  not redirect to /inscricao/"""
            self.assertEqual(200, self.response.status_code)

        def test_template(self):
            self.assertEqual(self.response, 'subscription/subscription_form.html')

        def test_has_form(self):
            form = self.response.context['form']
            self.assertInstance(form, SubscriptionForm)

        def test_has_errors(self):
            form = self.response.context['form']
            self.asserTrue(form.erros)

        def test_dont_save_subscription(self):
            self.assertFalse(Subscription.objects.exists())

@unittest.skip('To be removed.')
class SubscriveSuccessMessage(TestCase):
    def test_message(self):
        data = dict(name='Luiz Arthur', cpf='12345678907', email='herique@bastos.net', phone='99-99999-9999')
        response = self.client.post('/inscricao/', data, follow=True) # follow = True vai seguir o redirect
        self.assertContains(response, 'Inscrição realizada com sucesso')
