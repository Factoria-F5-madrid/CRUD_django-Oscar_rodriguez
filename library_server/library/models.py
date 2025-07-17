from django.db import models
from categories.models import Category

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.TextField()
    publication_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    categories = models.ManyToManyField(Category, related_name='categories')

    def __str__(self):
        return self.title
