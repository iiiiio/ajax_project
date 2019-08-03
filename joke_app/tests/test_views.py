from django.test import TestCase


class IndexTest(TestCase):
    def test_index_renders_joke_page(self):
        response = self.client.get('/joke_app/')
        self.assertTemplateUsed(response, 'joke_app/index.html')
