from django.test import TestCase


class IndexTest(TestCase):
    def test_index_renders_joke_page(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'index.html')
