from rest_framework import serializers
from .models import FitnessClass,ClassBooking
from zoneinfo import ZoneInfo

class FitnesClassSerilaizer(serializers.ModelSerializer):
    class Meta:
        model=FitnessClass
        fields=['id', 'name', 'instructor', 'datetime', 'available_slots']

class ClassBookingSerializer(serializers.ModelSerializer):
     class_name = serializers.CharField(source='fitness_class.name', read_only=True)
     instructor = serializers.CharField(source='fitness_class.instructor', read_only=True)
     datetime = serializers.SerializerMethodField()
     class Meta:
         model=ClassBooking
         fields=['id','client_name','client_email','class_name','instructor','datetime']

     def get_datetime(self, obj):
        request = self.context.get('request')
        tz_param = request.query_params.get('tz', 'Asia/Kolkata') if request else 'Asia/Kolkata'

        try:
            tz = ZoneInfo(tz_param)
        except:
            tz = ZoneInfo('Asia/Kolkata')  

        return obj.fitness_class.datetime.astimezone(tz).isoformat()