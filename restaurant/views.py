from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from django.contrib.auth.models import User
from restaurant.models import Booking, Menu
from restaurant.serializers import BookingSerializer, MenuSerializer, UserSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


# Create your views here.
def index(request):
    return render(request, "index.html", {})


class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class UsersView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
