from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer


class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title='IceCream', price=80, inventory=100)
        Menu.objects.create(title='Pizza', price=12.50, inventory=20)
        Menu.objects.create(title='Pasta', price=15, inventory=30)

    def test_getall(self):
        response = self.client.get('/restaurant/menu/')
        items = Menu.objects.all()
        serialized = MenuSerializer(items, many=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serialized.data)
