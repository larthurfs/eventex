from datetime import datetime

from django.test import TestCase

from eventex.subscriptions.models import Subscription


class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name='Luiz Arthur',
            cpf='00000000000',
            email='luiz@neurondat.com',
            phone='71-999999999',
        )
        self.obj.save()

    def test_create(self):
        self.asseertTrue(Subscription.objects.exists())

    def test_created_at(self):

        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual('Luiz Arthur', str(self.obj))

    def test_paid_default_to_False(self):
        self.assertEqual(False, self.obj.paid)