from django.test import TestCase
from django.urls import reverse
from remarcable.models import Product, Category, Tag

from .models import Product, Tag, Category

class ProductListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        category1 = Category.objects.create(name="Construction")
        category2 = Category.objects.create(name="Tools")

        tag1 = Tag.objects.create(name="Heavy-duty")
        tag2 = Tag.objects.create(name="Portable")

        hammer = Product.objects.create(name='Hammer', description='Its a Hammer', category=category1)
        hammer.tags.set([tag1])

        drill = Product.objects.create(name='Drill', description='Its a Drill', category=category2)
        drill.tags.set([tag2])

        saw = Product.objects.create(name='Saw', description='Its a Saw', category=category1)
        saw.tags.set([tag1])

        wrench = Product.objects.create(name='Wrench', description='Its a wrench', category=category2)
        wrench.tags.set([tag2])

    def test_product_list_view_get(self):
        response = self.client.get(reverse('product_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'remarcable/product_list.html')

    def test_search_by_query(self):
        response = self.client.get(reverse('product_list') + '?q=hammer')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Hammer')
        self.assertNotContains(response, 'Drill')

    def test_filter_by_category(self):
        category1 = Category.objects.get(name='Construction')
        response = self.client.get(reverse('product_list') + f'?Category={category1.id}')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Hammer')
        self.assertContains(response, 'Saw')
        self.assertNotContains(response, 'Drill')

    def test_filter_by_tag(self):
        tag1 = Tag.objects.get(name='Heavy-duty')
        response = self.client.get(reverse('product_list') + f'?Tag={tag1.id}')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Hammer')
        self.assertContains(response, 'Saw')
        self.assertNotContains(response, 'Drill')

    def test_combined_search_and_filter(self):
        category1 = Category.objects.get(name='Construction')
        tag1 = Tag.objects.get(name='Heavy-duty')
        response = self.client.get(reverse('product_list') + f'?q=hammer&Category={category1.id}&Tag={tag1.id}')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Hammer')
        self.assertNotContains(response, 'Drill')


