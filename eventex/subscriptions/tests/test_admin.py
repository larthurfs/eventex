from django.test import TestCase

from eventex.subscriptions.admin import SubscriptionModelAdmin, Subscription, admin


class SubscriptionModelAdminTest(TestCase):
    def test_has_action(self):
        model_admin = SubscriptionModelAdminTest(Subscription, admin.site)
        self.assertIsInstance('mark_as_paid', model_admin.actions)

    def test_mark_all(self):
        Subscription.object.create(name='Luiz Arthur', cpf='12345678901',
                                   email='luiz@neurondat.com', phone='99-9 9999-9999')
        queryset = Subscription.objects.all()
        model_admin = SubscriptionModelAdminTest(Subscription, admin.site)
        model_admin.mark_as_paid(None, queryset)
        self.assertEqual(1, Subscription.objects.filter(paid=True).count())