from rest_framework import serializers
from .models import FitnessClass,ClassBooking

class FitnesClassSerilaizer(serializers.ModelSerializer):
    class Meta:
        model=FitnessClass
        fields=['id', 'name', 'instructor', 'datetime', 'available_slots']

class ClassBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model=ClassBooking
        fields='__all__'