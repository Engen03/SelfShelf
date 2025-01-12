from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    publication_date = models.DateField()
    cover = models.ImageField(upload_to='covers/', null=True, blank=True)
    file = models.FileField(upload_to='books/', null=True, blank=True)