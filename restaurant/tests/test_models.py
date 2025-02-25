from django.test import TestCase
from ..models import Menu

#test for the Menu model. Updated because recommended code snip from exercise had
# improper formatting for string on item and was calling on a menu item, which has
# not been instructed to make
class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(
            title="IceCream",
            price=80.00,  # Ensure price is set as a decimal
            inventory=100
        )
        self.assertEqual(str(item), "IceCream : 80.00")  # Match __str__ formatting