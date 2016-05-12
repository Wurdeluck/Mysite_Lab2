from django import forms
from attendance.models import Book
from attendance.models import Author
from attendance.models import Genre


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('name', 'birth_year')


class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ('name',)


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('name', 'author', 'genre', 'pages')