from django.contrib import admin
from .models import *

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['department']


@admin.register(StudentId)
class StudentIdAdmin(admin.ModelAdmin):
    list_display = ['student_id']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['department','student_id', 'student_name', 'student_email', 'student_age', 'student_address']

