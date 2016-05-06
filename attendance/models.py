from django.db import models


# Create your models here.
class Student(models.Model):
    st_id = models.IntegerField()
    name = models.CharField(
        max_length=255,
    )
    group = models.CharField(
        max_length=255,
    )
    age = models.IntegerField()

    def __unicode__(self):
        return self.name


class Statistics(models.Model):
    gpa = models.IntegerField()


class Subject(models.Model):
    su_id = models.IntegerField()
    name = models.CharField(
        max_length=255,
    )

    def __unicode__(self):
        return self.name


class Score(models.Model):
    student_id = models.IntegerField()
    subject_id = models.IntegerField()
    score = models.IntegerField()

    def __unicode__(self):
        return self.score