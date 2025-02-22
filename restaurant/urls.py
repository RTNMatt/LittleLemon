#define URL route for index() view
from django.urls import path
from .views import BookingListCreateView, BookingDetailView, MenuListCreateView, MenuDetailView

urlpatterns = [
    path('bookings/', BookingListCreateView.as_view(), name='booking-list-create'),
    path('bookings/<int:pk>/', BookingDetailView.as_view(), name='booking-detail'),
    path('menu/', MenuListCreateView.as_view(), name='menu-list-create'),
    path('menu/<int:pk>/', MenuDetailView.as_view(), name='menu-detail'),
]
