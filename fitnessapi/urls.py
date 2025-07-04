from django.urls import path
from .views import FitnessClassList,FitnesClassBooking,BookingListview

urlpatterns = [
    path('classes/',FitnessClassList.as_view(),name='class_list'),
    path('booking/',FitnesClassBooking.as_view(),name='class_booking'),
    path('bookings/<str:email>/',BookingListview.as_view(),name='bookings_listb_by_mail')
]
