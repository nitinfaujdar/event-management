from django.urls import path
from .views import CreateEventView, ListUpcomingEventsView, RegisterAttendeeView, ListAttendeesView

urlpatterns = [
    path('events', CreateEventView.as_view(), name='create_event'),
    path('events/', ListUpcomingEventsView.as_view(), name='list_events'),
    path('events/<int:event_id>/register', RegisterAttendeeView.as_view(), name='register_attendee'),
    path('events/<int:event_id>/attendees', ListAttendeesView.as_view(), name='event_attendees'),
]
