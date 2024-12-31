from rest_framework import serializers
from .models import Menu
from .models import Booking  # Assuming the Booking model is defined in models.py

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__' 

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'title', 'price', 'inventory']  # Include the fields from the Menu model
