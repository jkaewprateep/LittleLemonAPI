from django_test import TestCase
from LittleLemonAPI.models import Menu;


# TestCase class
class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(item, "IceCream : 80")


class MenuViewTest(TestCase):
    class TestCase:
        def setUp(self):
            Menu.objects.create(name="lion", sound="roar")
            Menu.objects.create(name="cat", sound="meow")

        def test_getall(self):
            item = Menu.objects.all()
            self.assertEqual(item, "IceCream : 80")
