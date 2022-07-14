from django.core.exceptions import ValidationError

def validate_cpf(value): # todos os validadores recebem apenas um valor
    if not value.isdigit():
        raise ValidationError('CPF deve conter apenas números', 'digits') #podemos criar um código para o erro

    if len(value) != 11:
        raise ValidationError('CPF deve ter 11 números', 'lenght')