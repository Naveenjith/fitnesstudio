from django.test import TestCase
from .models import FitnessClass,ClassBooking
from django.utils.timezone import now,timedelta

class BookingTestCase(TestCase):
    def setUp(self):
        self.class1 = FitnessClass.objects.create(
            name='Yoga',
            instructor='Alice',
            datetime=now() + timedelta(days=1),
            total_slots=10,
            available_slots=10
        )

    def test_booking_creation(self):
        ClassBooking.objects.create(
            fitness_class=self.class1,
            client_name='John Doe',
            client_email='john@example.com'
        )
        self.class1.available_slots -= 1  
        self.class1.save()
        self.class1.refresh_from_db()
        self.assertEqual(self.class1.available_slots, 9)

