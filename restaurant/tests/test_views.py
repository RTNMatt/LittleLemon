from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from restaurant.models import Menu, Booking

class MenuItemViewTest(TestCase):
    def setUp(self):
        """Set up test data before each test."""
        self.client = APIClient()

        # Create a test user for authentication
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.client.force_authenticate(user=self.user)  # Authenticate the test client

        # Create menu items
        self.menu_item1 = Menu.objects.create(title="Pizza", price=12.99, inventory=50)
        self.menu_item2 = Menu.objects.create(title="Burger", price=8.50, inventory=30)
        self.menu_url = "/restaurant/menu/"  # Update with actual endpoint

    def test_get_all_menu_items(self):
        """Test retrieving the list of menu items."""
        response = self.client.get(self.menu_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_single_menu_item(self):
        """Test retrieving a single menu item."""
        response = self.client.get(f"{self.menu_url}{self.menu_item1.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Pizza")

    def test_create_menu_item(self):
        """Test creating a new menu item."""
        data = {"title": "Pasta", "price": 10.99, "inventory": 20}
        response = self.client.post(self.menu_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Menu.objects.count(), 3)

    def test_update_menu_item(self):
        """Test updating an existing menu item."""
        update_data = {"title": "Updated Pizza", "price": 14.99, "inventory": 45}
        response = self.client.put(f"{self.menu_url}{self.menu_item1.id}/", update_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.menu_item1.refresh_from_db()
        self.assertEqual(self.menu_item1.title, "Updated Pizza")

    def test_delete_menu_item(self):
        """Test deleting a menu item."""
        response = self.client.delete(f"{self.menu_url}{self.menu_item1.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Menu.objects.count(), 1)


class BookingViewSetTest(TestCase):
    def setUp(self):
        """Set up test data for BookingViewSet."""
        self.client = APIClient()

        # Create test user and authenticate
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.client.force_authenticate(user=self.user)  # Authenticate test client

        # Create booking
        self.booking = Booking.objects.create(name="John Doe", no_of_guests=4)
        self.booking_url = "/restaurant/tables/"  # Update with actual endpoint

    def test_get_all_bookings(self):
        """Test retrieving all bookings."""
        response = self.client.get(self.booking_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_booking(self):
        """Test creating a new booking."""
        data = {"name": "Alice", "no_of_guests": 2}
        response = self.client.post(self.booking_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Booking.objects.count(), 2)

    def test_update_booking(self):
        """Test updating a booking."""
        update_data = {"name": "Updated Name", "no_of_guests": 5}
        response = self.client.put(f"{self.booking_url}{self.booking.id}/", update_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.booking.refresh_from_db()
        self.assertEqual(self.booking.name, "Updated Name")

    def test_delete_booking(self):
        """Test deleting a booking."""
        response = self.client.delete(f"{self.booking_url}{self.booking.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Booking.objects.count(), 0)