from django.shortcuts import render, get_object_or_404, redirect
from .models import Booking, Menu
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'index.html', {})

# View to list all bookings
def booking_list(request):
    bookings = Booking.objects.all()
    return render(request, 'booking_list.html', {'bookings': bookings})

# View to list all menu items
def menu_list(request):
    menus = Menu.objects.all()
    return render(request, 'menu_list.html', {'menus': menus})

# View to view a specific booking
def booking_detail(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    return render(request, 'booking_detail.html', {'booking': booking})

# View to view a specific menu item
def menu_detail(request, menu_id):
    menu = get_object_or_404(Menu, id=menu_id)
    return render(request, 'menu_detail.html', {'menu': menu})

# View to create a new booking
def booking_create(request):
    if request.method == 'POST':
        name = request.POST['name']
        no_of_guests = request.POST['no_of_guests']
        booking_date = request.POST['booking_date']
        Booking.objects.create(name=name, no_of_guests=no_of_guests, booking_date=booking_date)
        return redirect('booking_list')
    return render(request, 'booking_form.html')

# View to create a new menu item
def menu_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        price = request.POST['price']
        inventory = request.POST['inventory']
        Menu.objects.create(title=title, price=price, inventory=inventory)
        return redirect('menu_list')
    return render(request, 'menu_form.html')