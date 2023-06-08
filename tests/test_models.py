from django.test import TestCase
from restaurant.serializers import MenuSerializer
from restaurant.models import Menu
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class MenuTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="Fish", price=10, inventory=10)
        Menu.objects.create(title="Chicken", price=8, inventory=1)
        Menu.objects.create(title="Steak", price=11, inventory=14)

        self.user = User.objects.create(username="tester")
        self.token = Token.objects.create(user=self.user)

    def test_get_item(self):
        item = Menu.objects.create(title="Ice Cream", price=20, inventory=5)
        self.assertEqual(item.__str__(), "Ice Cream : 20")

    def test_get_all(self):
        headers = {"Authorization": f"Token {self.token.key}"}
        response = self.client.get("/restaurant/menu/", headers=headers)
        self.assertEqual(response.status_code, 200)

        serializer = MenuSerializer(instance=Menu.objects.all(), many=True)
        expected = serializer.data

        self.assertEqual(response.data, expected)
