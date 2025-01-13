from django.shortcuts import render
from rest_framework import serializers
from rest_framework import viewsets
from .models import Book, User, Transaction
from .serializers import BookSerializer, UserSerializer, TransactionSerializer
from rest_framework import status
from rest_framework.response import Response

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def perform_create(self, serializer):
        # Ensure ISBN is unique
        isbn = serializer.validated_data.get('isbn')
        if Book.objects.filter(isbn=isbn).exists():
            raise serializers.ValidationError("ISBN already exists.")
        super().perform_create(serializer)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def create(self, request, *args, **kwargs):
        book_id = request.data.get('book')
        user_id = request.data.get('user')

        book = Book.objects.get(id=book_id)
        if book.available_copies < 1:
            return Response({"detail": "No available copies."}, status=status.HTTP_400_BAD_REQUEST)

        # Decrease available copies
        book.available_copies -= 1
        book.save()

        transaction = Transaction.objects.create(user_id=user_id, book=book)
        return Response(self.get_serializer(transaction).data, status=status.HTTP_201_CREATED)

