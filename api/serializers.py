from rest_framework import serializers
from .models import Event, Attendee
from django.utils.timezone import get_current_timezone
from pytz import timezone as pytz_timezone

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class AttendeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendee
        fields = ['name', 'email']

class EventDetailSerializer(serializers.ModelSerializer):
    attendees = AttendeeSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = '__all__'
