from django.shortcuts import render

from rest_framework import generics, permissions
from .models import Event, Attendee, Task
from .serializers import EventSerializer, AttendeeSerializer, TaskSerializer

class EventListCreateView(generics.ListCreateAPIView):
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Only return events for the current user
        return Event.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Assign the current user to the event
        serializer.save(user=self.request.user)

class EventDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]

class AttendeeListCreateView(generics.ListCreateAPIView):
    serializer_class = AttendeeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        event_id = self.kwargs['event_pk']
        return Attendee.objects.filter(event_id=event_id)

    def perform_create(self, serializer):
        event = Event.objects.get(pk=self.kwargs['event_pk'])
        serializer.save(event=event)

class AttendeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AttendeeSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'pk'

    def get_queryset(self):
        return Attendee.objects.all()

class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        event_id = self.kwargs['event_pk']
        return Task.objects.filter(event_id=event_id)

    def perform_create(self, serializer):
        event = Event.objects.get(pk=self.kwargs['event_pk'])
        serializer.save(event=event)

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'pk'

    def get_queryset(self):
        return Task.objects.all()
