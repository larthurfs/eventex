from django.core.exceptions import ValidationError
from django.test import TestCase

from eventex.core.models import Speaker, Contact


class ContactModelTest(TestCase):
    def setUp(self):
        self.speaker = Speaker.objects.create(
            name = 'Luiz Arthur',
            slug = 'luiz-arthur',
            photo = 'http://hbn.link/la-pic'
        )
    def test_email(self):
        contact = Contact.objects.create(speaker=self.speaker, kind='E', value='luiz@neurondat.com')

        self.assertTrue(Contact.objects.exists())

    def test_email(self):
        contact = Contact.objects.create(speaker=self.speaker, kind='P', value='7199999999')

        self.assertTrue(Contact.objects.exists())

    def test_choices(self):
        contact = Contact(speaker=self.speaker, kind='A', value='B')
        self.assertRaises(ValidationError, contact.full_clean)

    def test_str(self):
        contact = Contact(speaker=self.speaker, kind='E', value='luiz@neurondat.com')
        self.assertEqual('luiz@neurondat.com', str(contact))



class ContactManagerTest(TestCase):
    def setUp(self):
        s = Speaker.objects.create(
            name='Luiz Arthur',
            slug='luiz-arthur',
            photo='http://hbn.link/la-pic',
        )

        s.contact_set.create(kind=Contact.EMAIL, value='luiz@neurondat.com')
        s.contact_set.create(kind=Contact.PHONE, value='71-999999999')

    def test_emails(self):
        qs = Contact.objects.emails()
        #qs = Contact.emails.all()
        expected = ['luiz@neurondat.com']
        self.assertQuerysetEqual(qs, expected, lambda o: o.value)

    def test_phones(self):
        qs = Contact.objects.phones()
        #qs = Contact.phones.all()
        expected = ['71-999999999']
        self.assertQuerysetEqual(qs, expected, lambda o: o.value)
