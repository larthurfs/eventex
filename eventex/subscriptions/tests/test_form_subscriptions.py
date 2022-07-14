from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm


class SubscribeForm(TestCase):
    def setUp(self):
        self.form = SubscriptionForm()

    def test_form_has_fields(self):
        """Form must have 4 fields"""
        expected = ['nmae', 'cpf', 'email', 'phone']
        self.assertSequenceEqual(expected, list(self.form.fields))

    def test_cpf_is_digit(self):

        form = self.make_validated_form(cpf='ABCD5678901')
        self.assertFormErrorMessage(form, 'cpf', 'CPF deve conter apenas números.')

    def test_cpf_has_11_digitis(self):
        form = self.make_validated_form(cpf='1234')
        self.assertFormErrorMessage(form, 'cpf', 'CPF deve ter 11 números.')

    def test_name_must_be_capitazed(self):
        form = self.make_validated_form(name='LUIZ arthur')
        self.assertEqual('Luiz Arthur', form.cleaned_data['name'])

    def test_email_is_optional(self):
        form = self.make_validated_form(email='')
        self.assertFalse(form.errors)

    def test_phone_is_optional(self):
        form = self.make_validated_form(phone='')
        self.assertFalse(form.errors)

    def test_must_inform_email_or_phone(self):
        form = self.make_validated_form(email='', phone='')
        self.assertListEqual(['__all__'], list(form.errors))

    def assertFormErrorMessage(self, form, field, msg):
        errors = form.errors
        errors_list = errors[field]

        self.assertListEqual([msg], errors_list)


    def make_validated_form(self, **kwargs):
        valid = dict(name='Luiz Arthur', cpf='12345678901', email='luiz@neurondat.com', phone='99-99999999')
        data = dict(valid, **kwargs)
        form = SubscriptionForm(data)
        form.is_valid()
        return form