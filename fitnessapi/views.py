from django.shortcuts import render
from rest_framework.views import APIView
from .models import FitnessClass,ClassBooking
from .serializers import FitnesClassSerilaizer,ClassBookingSerializer
from django.utils.timezone import localtime
from rest_framework.response import Response
import logging
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from zoneinfo import ZoneInfo


logger=logging.getLogger(__name__)

class FitnessClassList(APIView):
    def get(self, request):
        tz_param = request.query_params.get('tz', 'Asia/Kolkata')
        try:
            user_tz = ZoneInfo(tz_param)
        except:
            return Response({"error": "Invalid timezone"}, status=400)

        classes = FitnessClass.objects.filter(datetime__gte=localtime())
        data = []
        for x in classes:
            # Convert to requested timezone
            converted_time = x.datetime.astimezone(user_tz).isoformat()
            data.append({
                "id": x.id,
                "name": x.name,
                "instructor": x.instructor,
                "datetime": converted_time,
                "available_slots": x.available_slots
            })
        return Response(data)
    
class FitnesClassBooking(APIView):
    def post(self,request):
        try:
            class_id=request.data.get('fitness_class')
            name=request.data.get('client_name')
            email=request.data.get('client_email')

            if not all([class_id,name,email]):
                return Response({"error":"All Fields Required"},status=status.HTTP_400_BAD_REQUEST)
            
            try:
                fitness_class=FitnessClass.objects.get(id=class_id)
            except ObjectDoesNotExist:
                return Response({"error":"Fitness Class Not Found"},status=status.HTTP_404_NOT_FOUND)
            
            if fitness_class.available_slots <=0:
                return Response({"error":"NO Available Slots"},status=status.HTTP_400_BAD_REQUEST)
            
            ClassBooking.objects.create(fitness_class=fitness_class,client_name=name,client_email=email)
            fitness_class.available_slots -=1
            fitness_class.save()
            logger.info(f"Booking Confirmed for {email} in class {fitness_class.id}")
            return Response({"Response":"Booking Seccessful"},status=status.HTTP_201_CREATED)

        except Exception as e:
            logger.error(f"Booking Failed: {e}")
            return Response({"error":"Booking Failed"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class BookingListview(APIView):
    def get(self,request,email):
        if not email:
            return Response({"error":"Email Parameter Is Required"},status=status.HTTP_400_BAD_REQUEST)
        booking=ClassBooking.objects.filter(client_email=email)
        serializer=ClassBookingSerializer(booking,many=True,context={'request': request})
        return Response(serializer.data)

