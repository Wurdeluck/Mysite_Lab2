from django.contrib import admin

# Register your models here.
from attendance.models import Student
from attendance.models import Score
from attendance.models import Subject
from attendance.models import Statistics


class StudentAdmin(admin.ModelAdmin):
    fields = ['st_id', 'name']
    list_display = ('st_id', 'name')

admin.site.register(Student, StudentAdmin)


class ScoreAdmin(admin.ModelAdmin):
    fields = ['student_id', 'subject_id', 'score']
    list_display = ('student_id', 'subject_id', 'score')

admin.site.register(Score, ScoreAdmin)


class SubjectAdmin(admin.ModelAdmin):
    fields = ['su_id', 'name']
    list_display = ('su_id', 'name')

admin.site.register(Subject, SubjectAdmin)


admin.site.register(Statistics)
