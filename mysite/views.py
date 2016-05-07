# -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView
import random
import numpy
from django.db import models
from attendance.models import Book
from attendance.models import Author
from attendance.models import Genre


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update(
            {
                'books':
                    [
                        {
                            'name': book.name,
                            'author': book.author,
                            'genre': book.genre,
                        } for book in Book.objects.all()
                    ],
                'authors':
                    [
                        {
                            'name': author.name,
                            'birth_year': author.birth_year,
                        } for author in Author.objects.all()
                        ],
                'genres':
                    [
                        {
                            'name': genre.name,
                        } for genre in Genre.objects.all()
                        ],

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







