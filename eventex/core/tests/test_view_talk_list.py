from django.test import TestCase
from django.shortcuts import resolve_url as r

from eventex.core.models import Talk, Speaker, Course


class TalkListGet(TestCase):
    def setUp(self):
        t1 = Talk.objects.create(title='Título da Palestra', star='10:00', description='Descrição da palestra')
        t2 = Talk.objects.create(title='Título da Palestra', star='13:00', description='Descrição da palestra')
        c1 = Course.objects.create(title='Título do Curso', star='09:00', description='Descrição do curso', slots=20)

        speaker = Speaker.objects.create(name='Luiz Arthur', slug='luiz-arthur', website='http//luizarthur.net')

        t1.speakers.add(speaker)
        t2.speakers.add(speaker)
        c1.speakers.add(speaker)

        self.response = self.client.get(r('talk_list'))

    def test_get(self):
        self.assertEqual(200,  self.response.status_code)

    def test_template(self):

        self.assertTemplateUsed(self.response, 'core/talk_list.html')

    def test_html(self):
        contents = [
            (2, 'Título da Palestra'),
            (1, '10:00'),
            (1, '13:00'),
            (2, '/palestrante'),
            (2, 'Luiz Arthur'),
            (1, 'Título do Curso'),
            (1, '09:00'),
            (1, 'Descrição do curso'),
        ]

        for count, expected in contents:
            with self.subTest():
                self.assertContains(self.response, expected, count)

    def test_context(self):
        varibles = ['morning_talks', 'afternoon_talks', 'courses']

        for key in varibles:
            with self.subTest():
                self.assertIn(key, self.response.context)