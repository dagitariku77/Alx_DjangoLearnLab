from rest_framework import serializers
from .models import Event, Attendee, Task
from django.contrib.auth.models import User

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
        read_only_fields = ('user',)  # User should be assigned on creation

class AttendeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendee
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'