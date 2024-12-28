from rest_framework import serializers
from .models import Book, Author

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name']

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'publication_date']
        
    def create(self, validated_data):
        author_name = validated_data.pop('author').get("name")
        title = validated_data.get("title")
        publication_date = validated_data.get("publication_date")
        
        try:
            author = Author.objects.get(name=author_name)
        except Author.DoesNotExist:
            raise serializers.ValidationError({"author": "Автор не существует"})

        book = Book.objects.create(author=author, title=title, publication_date=publication_date)
        return book