from django.contrib import messages
from django.core import mail
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.template.loader import render_to_string
from django.conf import settings
from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription


def subscribe(request):
    if request.method == 'POST':
        return create(request)
    else:
        return new(request)


def create(request):
    form = SubscriptionForm(request.POST)

    if not form.is_valid():
        return render(request, 'subscriptions/subscription_form.html', {'form': form})

    subscription = form.save()

    # Envia Email
    _send_email('Confirmação de Inscrição', settings.DEFAULT_FROM_EMAIL, subscription.email,'subscriptions/subscription_email.txt' , {'subscription':subscription})

    return HttpResponseRedirect(f'/inscricao/{subscription.pk}/')





def new(request):
    return render(request, 'subscriptions/subscription_form.html', {'form': SubscriptionForm()})


def _send_email(template_name, context, subject, from_, to):
    body = render_to_string(template_name, context)
    mail.send_mail = (subject, body, settings.DEFAULT_FROM_EMAIL, [from_, to])


def detail(request, pk):
    try:
        subscription = Subscription.objects.get(pk=pk)
    except Subscription.DoesNotExist:
        raise Http404

    return render(request, 'subscriptions/subscription_detail.html',{'subscription':subscription})
