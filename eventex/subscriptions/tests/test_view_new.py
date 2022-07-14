from django.test import TestCase



class TemplateRegressionTest(TestCase):
    def test_template_has_non_fields_errors(self):
        invalid_data = dict(name='Luiz Arthur', cpf='12345678901')
        response = self.client.post(r('subscriptions:new'), invalid_data)

        self.assertContains(response, '<ul class="errorlist nonfield"')