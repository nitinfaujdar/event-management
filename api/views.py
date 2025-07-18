from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils.timezone import now
from django.shortcuts import get_object_or_404
from pytz import timezone as pytz_timezone
from .models import Event, Attendee
from .serializers import EventSerializer, AttendeeSerializer, EventDetailSerializer

class CreateEventView(generics.CreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class ListUpcomingEventsView(generics.ListAPIView):
    queryset = Event.objects.filter(end_time__gte=now()).order_by('start_time')
    serializer_class = EventSerializer

class RegisterAttendeeView(APIView):
    def post(self, request, event_id):
        event = get_object_or_404(Event, id=event_id)

        if event.attendees.count() >= event.max_capacity:
            return Response({"error": "Event is at full capacity"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = AttendeeSerializer(data=request.data)
        if serializer.is_valid():
            if Attendee.objects.filter(event=event, email=serializer.validated_data['email']).exists():
                return Response({"error": "Attendee already registered with this email"}, status=status.HTTP_400_BAD_REQUEST)
            serializer.save(event=event)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ListAttendeesView(generics.ListAPIView):
    serializer_class = AttendeeSerializer

    def get_queryset(self):
        event_id = self.kwargs['event_id']
        return Attendee.objects.filter(event_id=event_id)

    def list(self, request, *args, **kwargs):
        queryset = self.paginate_queryset(self.get_queryset().order_by('id'))
        if queryset is not None:
            serializer = self.get_serializer(queryset, many=True)
            return self.get_paginated_response(serializer.data)
        return Response({"attendees": serializer.data})
