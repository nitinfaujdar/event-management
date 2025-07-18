from django.test import TestCase
from .models import Event, Attendee
from django.utils import timezone
from datetime import timedelta

class EventTest(TestCase):
    def test_create_event(self):
        start = timezone.now()
        end = start + timedelta(hours=2)
        event = Event.objects.create(name="Test", location="Delhi", start_time=start, end_time=end, max_capacity=100)
        self.assertEqual(Event.objects.count(), 1)
