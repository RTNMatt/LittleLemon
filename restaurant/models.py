from django.db import models

# Create your models here.
class Booking(models.Model):
    # ID field (integer with a limit of 11 digits)
    id = models.IntegerField(11)
    # Name of the booking (max length of 255 characters)
    name = models.CharField(max_length=255)
    # Number of guests (integer with a limit of 6 digits)
    no_of_guests = models.PositiveIntegerField()  # PositiveIntegerField is typically used for non-negative integers
    # Booking date and time
    booking_date = models.DateTimeField()
    # Optionally, define a string representation for the model
    def __str__(self):
        return f"Booking for {self.name} on {self.booking_date}"

class Menu(models.Model):
    # ID field (integer with a limit of 5 digits)
    id = models.IntegerField(5)
    # Title of the menu item (max length of 255 characters)
    title = models.CharField(max_length=255)
    # Price of the menu item (decimal with 10 digits, 2 after the decimal point)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # Inventory of the menu item (integer with a limit of 5 digits)
    inventory = models.PositiveIntegerField()
    # Optionally, define a string representation for the model
    def __str__(self):
        return f"{self.title} - ${self.price}"