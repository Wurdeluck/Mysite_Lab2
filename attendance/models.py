from django.db import models


# Create your models here.


class Author(models.Model):
    name = models.CharField(
        max_length=255,
    )
    birth_year = models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(
        max_length=255,
    )

    # def count_gpas(self):
    #     return sum([x for x in range(10)])
    #
    def __str__(self):
        return self.name


class Book(models.Model):
    genre = models.ForeignKey(Genre)
    author = models.ForeignKey(Author)
    name = models.CharField(
        max_length=255,
    )
    pages = models.PositiveIntegerField()

    def __str__(self):
        return self.name
