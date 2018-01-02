from django.test import TestCase
#from django.core.urlresolvers import reverse
from rest_framework.reverse import reverse


class ProductsTest(TestCase):
    def test_category_list(self):
        response = self.client.get(reverse('products_api:category_list_create'))
        self.assertEqual(response.status_code, 200)