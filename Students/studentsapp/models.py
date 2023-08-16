from django.db import models
from django.db.models.query import QuerySet

"""Creating model manager"""
class StudentManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted = False)


class Department(models.Model):
    department = models.CharField(max_length=100)

    def __str__(self) -> str:
         return self.department
    
    class Meta:
        ordering = ['department']


class StudentId(models.Model):
    student_id = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.student_id

class Student(models.Model):
    department = models.ForeignKey(Department, related_name='depart', on_delete=models.CASCADE)
    student_id = models.OneToOneField(StudentId, related_name='studentid', on_delete=models.CASCADE)
    student_name = models.CharField(max_length=100)
    student_email = models.EmailField(unique=True)
    student_age = models.IntegerField(default=18)
    student_address = models.TextField()
    is_deleted = models.BooleanField(default=False)

    """calling model manager"""
    objects = StudentManager()
    admin_objects = models.Manager()

    def __str__(self) ->str:
        return self.student_name
    
    class Meta:
        ordering = ['student_name']
        verbose_name = "Student"
