from django.contrib import admin

# Register your models here.
from attendance.models import Book
from attendance.models import Author
from attendance.models import Genre


class BookAdmin(admin.ModelAdmin):
    fields = ['genre', 'author', 'name', 'pages']
    list_display = ('genre', 'author', 'name', 'pages')

admin.site.register(Book, BookAdmin)


class AuthorAdmin(admin.ModelAdmin):
    fields = ['name', 'birth_year']
    list_display = ('name', 'birth_year')
    # exclude = ('student_id', 'subject_id',)

admin.site.register(Author, AuthorAdmin)


admin.site.register(Genre)


