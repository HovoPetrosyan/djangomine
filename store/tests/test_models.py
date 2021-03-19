from django.test import TestCase

# Create your tests here.
from store.models import Category, Product


class TestCategoriesModel(TestCase):

    def setUp(self):
        self.data1 = Category.objects.create(name='django', slug='django')

    def test_category_model_entry(self):
        """
        test category model data inserton/types/fields
        :return:
        """
        data = self.data1
        self.assertTrue(isinstance(data, Category))

    def test_category_model_entry(self):
        """
        test category model return name
        :return:
        """
        data = self.data1
        self.assertEqual(str(data), 'django')
