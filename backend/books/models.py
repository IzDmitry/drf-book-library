from django.db import models


class Author(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'


class Book(models.Model):
    name = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    date = models.DateField()
    isbn = models.TextField()

    def __str__(self) -> str:
        return self.name
