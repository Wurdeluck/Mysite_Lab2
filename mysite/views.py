# -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView
from django.shortcuts import render, redirect, get_object_or_404
import random
import numpy
from django.db import models
from attendance.models import Book
from attendance.models import Author
from attendance.models import Genre
from .forms import AuthorForm
from .forms import GenreForm
from .forms import BookForm


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update(
            {
                'books': Book.objects.all(),
                'authors': Author.objects.all(),
                'genres':  Genre.objects.all(),

            }
        )
        return context

# Describe all classes


class Student(object):

    def __init__(self, id, person, group, age):
        self.id = id
        self.person = person
        self.group = group
        self.age = age

    def count_gpas(self):
        return sum([score.value for score in scores if score.student_id == self.id])/len(subjects)


class Subject(object):
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def get_scores(self, student):
        return [score.value for score in scores if score.student_id == student.id and score.subject_id == self.id][0]


class Score(object):
    def __init__(self, student_id, subject_id, value):
        self.student_id = student_id
        self.subject_id = subject_id
        self.value = value


# Create all students and list of them

a0 = Student(id=1, person='Коля', group='714', age=20)
a1 = Student(id=2, person='Igor', group='714', age=19)
a2 = Student(id=3, person='Ignat', group='714', age=19)
a3 = Student(id=4, person='Oleg', group='714', age=21)
a4 = Student(id=5, person='Leha', group='714', age=18)
a5 = Student(id=6, person='Marina', group='714', age=29)
a6 = Student(id=7, person='Ahmet', group='714', age=19)
a7 = Student(id=8, person='Вениамин', group='714', age=18)
a8 = Student(id=9, person='Один', group='714', age=19)
a9 = Student(id=10, person='Весемир', group='714', age=34)
students = [a0, a1, a2, a3, a4, a5, a6, a7, a8, a9]

# Create all subjects and list of them

TiMP = Subject(id=1, name='TiMP')
PSSM = Subject(id=2, name='PSSM')
TI = Subject(id=3, name='TI')
BOS = Subject(id=4, name='BOS')
SPORT = Subject(id=5, name='SPORT')
subjects = [TiMP, PSSM, TI, BOS, SPORT]

# Create all scores

scores = [Score(student_id=student.id, subject_id=subject.id, value=random.randint(0, 5))
          for subject in subjects
          for student in students]

# Find best and worst students

best = [student.person for student in students if student.count_gpas() >= 4.5]
worst = [student.person for student in students if student.count_gpas() <= 2.5]


def author_new(request):
    form = AuthorForm(request.POST)
    if form.is_valid():
        post = form.save(commit=False)
        post.save()
        return redirect('/')
    else:
        form = AuthorForm()
    return render(request, 'author_new.html', {'form': form})


def book_new(request):
    form = BookForm(request.POST)
    if form.is_valid():
        post = form.save(commit=False)
        post.save()
        return redirect('/')
    else:
        form = BookForm()
    return render(request, 'book_new.html', {'form': form})


def genre_new(request):
    form = GenreForm(request.POST)
    if form.is_valid():
        post = form.save(commit=False)
        post.save()
        return redirect('/')
    else:
        form = GenreForm()
    return render(request, 'genre_new.html', {'form': form})


def author_edit(request, pk):
    author = Author.objects.get(pk=pk)
    if request.method == "POST":
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            # author = form.save(commit=False)
            form.save()
            return redirect('/')
    else:
        form = AuthorForm(instance=author)
    return render(request, 'author_new.html', {'form': form})


def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            book = form.save(commit=False)
            form.save()
            return redirect('/')
    else:
        form = BookForm(instance=book)
    return render(request, 'book_new.html', {'form': form})


def genre_edit(request, pk):
    print(11111111111111)
    genre = get_object_or_404(Genre, pk=pk)
    if request.method == "POST":
        form = GenreForm(request.POST, instance=genre)
        if form.is_valid():
            genre = form.save(commit=False)
            form.save()
            return redirect('/')
    else:
        form = GenreForm(instance=genre)
    return render(request, 'genre_new.html', {'form': form})


def author_delete(request, pk):
    delete = get_object_or_404(Author, pk=pk)
    if request.method == "POST":
        form = AuthorForm(request.POST, instance=delete)
        if form.is_valid():
            # delete = form.save(commit=False)
            delete.delete()
            return redirect('/')
    else:
        form = AuthorForm(instance=delete)
    return render(request, 'author_new.html', {'form': form})









