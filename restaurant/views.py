from rest_framework import generics
from .models import Booking, Menu
from .serializers import BookingSerializer, MenuSerializer
from rest_framework import viewsets

# Booking ViewSet
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

# List and Create Menu Items. ListCreateAPIView would be a good choice for this view if using Django Rest Framework instead of Gjango Generic Views
class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

# Retrieve, Update, and Delete a Single Menu Item
class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer