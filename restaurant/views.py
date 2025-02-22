from rest_framework import generics
from .models import Booking, Menu
from .serializers import BookingSerializer, MenuSerializer

# List and Create Bookings. ListCreateAPIView would be a good choice for this view if using Django Rest Framework instead of Gjango Generic Views
class BookingListCreateView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

# Retrieve, Update, and Delete a Single Booking
class BookingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

# List and Create Menu Items. ListCreateAPIView would be a good choice for this view if using Django Rest Framework instead of Gjango Generic Views
class MenuListCreateView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

# Retrieve, Update, and Delete a Single Menu Item
class MenuDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer