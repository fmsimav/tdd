from django.test import TestCase
from django.urls import resolve
from lists import views
from lists.views import home_page

from django.http import HttpRequest
from django.template.loader import render_to_string

class HomePageTest(TestCase):

    def test_uses_home_template(self):

        response = self.client.get('/')
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.strip().endswith('</html>'))

        self.assertTemplateUsed(response, 'lists/home.html')
