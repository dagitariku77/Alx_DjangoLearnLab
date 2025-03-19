from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import (
    EventListCreateView,
    EventDetailView,
    AttendeeListCreateView,
    AttendeeDetailView,
    TaskListCreateView,
    TaskDetailView,
)

urlpatterns = [
    path('events/', EventListCreateView.as_view(), name='event-list-create'),
    path('events/<int:pk>/', EventDetailView.as_view(), name='event-detail'),
    path('events/<int:event_pk>/attendees/', AttendeeListCreateView.as_view(), name='attendee-list-create'),
    path('attendees/<int:pk>/', AttendeeDetailView.as_view(), name='attendee-detail'),
    path('events/<int:event_pk>/tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('api-token-auth/', obtain_auth_token), # Add this line
]