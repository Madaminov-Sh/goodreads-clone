from rest_framework import serializers

from .models import Book, Author, BookAuthor


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'first_name', 'last_name', 'email', 'bio')


class BookAuthorSerializer(serializers.ModelSerializer):
    # author = AuthorSerializer()

    class Meta:
        model = BookAuthor
        fields = "__all__"


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ['id', 'Bookauthor', 'title', 'description', 'isbn']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['Bookauthor'] = BookAuthorSerializer(instance.Bookauthor).data
        return representation
