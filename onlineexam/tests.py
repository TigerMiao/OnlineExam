from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from .views import home_page

class HomePageTest(TestCase):

    def test_root_url_resolve_to_home_page_view(self):
        self.assertEqual(resolve('/').func, home_page)

    def test_home_page_return_correct_html(self):
        request = HttpRequest()
        response = home_page(request)

        html = response.content.decode('utf-8')

        self.assertTrue(html.startswith('<html>'))
        self.assertIn("<h1>Hello, world. You're at mysite index.</h1>", html)
        self.assertTrue(html.endswith('</html>'))

