from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)

class Magazine(models.Model):
    name = models.CharField(max_length=100)

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    magazines = models.ManyToManyField(Magazine)