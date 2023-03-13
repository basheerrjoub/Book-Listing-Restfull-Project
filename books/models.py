from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    about = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13)

    def __str__(self):
        return f"{self.title} By {self.author}"
