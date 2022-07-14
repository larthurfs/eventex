from django import forms
from django.core.exceptions import ValidationError
from eventex.subscriptions.models import Subscription


class SubscriptionForm(forms.ModelForm):

    class Meta:
        model = Subscription
        fields = ['name', 'cpf', 'email', 'phone']

    def clean_name(self): # O formulario procura por qualquer metodo chamado por clean_ nome do campo e chama ele como complementa da validação!
        name = self.cleaned_data['name']
        return ' '.join([w.capitalize() for w in name.split()])

    def clean(self): # conseguimos avaliar o formulário depois do cleaned_data
        self.cleaned_data = super().clean()

        if not self.cleaned_data.get('email') and not self.cleaned_data.get('phone'):
            raise ValidationError('Informe seu e-mail ou telefone.')

        return self.cleaned_data