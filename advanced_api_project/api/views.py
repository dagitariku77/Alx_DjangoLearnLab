from django.shortcuts import render

from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

def perform_create(self, serializer):
        # Custom behavior on create: add a check for the publication year
        if serializer.validated_data['publication_year'] > datetime.now().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        serializer.save()


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_update(self, serializer):
        # Custom behavior on update: add a check for the publication year
        if 'publication_year' in serializer.validated_data and serializer.validated_data['publication_year'] > datetime.now().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        serializer.save()
