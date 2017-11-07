from django.test import TestCase
from django.urls import resolve
from lists import views
from lists.views import home_page

from django.http import HttpRequest
from django.template.loader import render_to_string
from lists.models import Item


class ItemModelTest(TestCase):

    def test_saving_and_retrieving_items(self):
        response = self.client.post('/', data={'item_text': 'A new list item'})

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual (new_item.text, 'A new list item')


class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'lists/home.html')

    def test_can_save_a_POST_request(self):
        response = self.client.post('/', data={'item_text': 'A new list item'})

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEquals (new_item.text, 'A new list item')

    def test_redirects_after_POST(self):
        response = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/lists/the-only-list-in-the-world/')

    def test_only_saves_items_when_necessary(self):
        self.client.get('/')
        self.assertEqual(Item.objects.count(), 0)


class ListViewTest(TestCase):

    def test_uses_list_template(self):
        response = self.client.get('/lists/the-only-list-in-the-world/')
        self.assertTemplateUsed(response, 'lists/list.html')

    def test_display_all_items(self):
        Item.objects.create(text='Itemsal 1')
        Item.objects.create(text='Itemsal 2')

        response = self.client.get('/lists/the-only-list-in-the-world/')
        self.assertContains(response, 'Itemsal 1')
        self.assertContains(response, 'Itemsal 2')