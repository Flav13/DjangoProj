from rest_framework import serializers

from bookLib.models import (
    Author,
    Book,
)

class BookSerializer(serializers.ModelSerializer):
    """
    Serializing all the Books
    """
    search_url = serializers.SerializerMethodField()
    class Meta:
        model = Book
        fields = ('id', 'title', 'isbn','search_url')
    
    def get_search_url(self, obj):
        return "http://www.isbnsearch.org/isbn/{}".format(obj.isbn)

class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializing all the Authors
    """
    books = BookSerializer(many=True,read_only=True)
    class Meta:
        model = Author
        fields = ('id', 'first_name', 'last_name','books')


