import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from django.utils.timezone import now, timedelta
from api.models import Event

@pytest.mark.django_db
def test_create_event():
    client = APIClient()
    url = reverse("create_event")
    data = {
        "name": "Test Event",
        "location": "Delhi",
        "start_time": (now() + timedelta(hours=1)).isoformat(),
        "end_time": (now() + timedelta(hours=3)).isoformat(),
        "max_capacity": 10
    }
    response = client.post(url, data, format="json")
    assert response.status_code == 201
    assert Event.objects.count() == 1

@pytest.mark.django_db
def test_register_attendee():
    from api.models import Attendee

    event = Event.objects.create(
        name="Demo",
        location="Mumbai",
        start_time=now() + timedelta(hours=1),
        end_time=now() + timedelta(hours=2),
        max_capacity=2
    )
    client = APIClient()
    url = f"/events/{event.id}/register"
    payload = {"name": "John", "email": "john@example.com"}

    response = client.post(url, payload, format="json")
    assert response.status_code == 201
    assert Attendee.objects.filter(event=event).count() == 1