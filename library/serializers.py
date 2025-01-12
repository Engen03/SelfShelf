from rest_framework import serializers
from .models import Book, Author

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name']

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    cover = serializers.ImageField(required=False)
    file = serializers.FileField(required=False)

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'publication_date', 'cover', 'file']
        
    def create(self, validated_data):
        author_name = validated_data.pop('author').get("name")
        title = validated_data.get("title")
        publication_date = validated_data.get("publication_date")
        cover = validated_data.get("cover")
        file = validated_data.get("file")

        try:
            author = Author.objects.get(name=author_name)
        except Author.DoesNotExist:
            raise serializers.ValidationError({"author": "Автор не существует"})

        book = Book.objects.create(author=author, title=title, publication_date=publication_date, cover=cover, file=file)
        return book

    def update(self, instance, validated_data):
        # Обновление данных книги
        author_data = validated_data.pop('author', None)  # Извлечение данных об авторе, если они переданы
        if author_data:
            author_name = author_data.get("name")
            try:
                author = Author.objects.get(name=author_name)
            except Author.DoesNotExist:
                raise serializers.ValidationError({"author": "Автор не существует"})
            instance.author = author  # Обновление автора книги

        # Обновление остальных полей книги
        instance.title = validated_data.get('title', instance.title)
        instance.publication_date = validated_data.get('publication_date', instance.publication_date)
        instance.cover = validated_data.get('cover', instance.cover)
        instance.file = validated_data.get('file', instance.file)

        # Сохранение изменений
        instance.save()
        return instance

class AuthorDetailedSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)
    
    class Meta():
        model = Author
        fields = ['id', 'name', 'books']