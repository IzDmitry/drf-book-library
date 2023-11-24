from rest_framework import serializers
from .models import Author, Book


class AuthorSerializer(serializers.ModelSerializer):
    """
    Сериализатор для объектов Author.
    """
    class Meta:
        model = Author
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    """
    Сериализатор для объектов Book.

    Метод create(self, validated_data) - Сохраняет книгу в базе данных
    Метод update(self, validated_data) - Обновляет книгу в базе данных
    Метод to_representation(self, instance) - Возвращает словарное
    представление модели
    """
    author = AuthorSerializer()

    class Meta:
        model = Book
        fields = '__all__'

    def create(self, validated_data):
        author_data = validated_data.pop('author')
        author, _ = Author.objects.get_or_create(**author_data)
        book = Book.objects.create(author=author, **validated_data)
        return book

    def update(self, instance, validated_data):
        author_data = validated_data.pop('author')
        author, _ = Author.objects.get_or_create(**author_data)
        instance.author = author
        instance.name = validated_data.pop('name')
        instance.date = validated_data.pop('date')
        instance.isbn = validated_data.pop('isbn')
        instance.save()
        return instance

    def to_representation(self, instance) -> dict:
        _dict: dict = {
            'id': instance.id,
            'name': instance.name,
            'author': f'{instance.author.first_name} '
                      f'{instance.author.last_name}',
            'date': instance.date,
            'isbn': instance.isbn,
        }
        return _dict
