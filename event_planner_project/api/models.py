from django.db import models

from django.contrib.auth.models import User

class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='events')
    name = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Attendee(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='attendees')
    name = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Task(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='tasks')
    description = models.TextField()
    due_date = models.DateField()
    status = models.CharField(max_length=50, default='Pending')  # e.g., 'Pending', 'In Progress', 'Completed'

    def __str__(self):
        return self.description
