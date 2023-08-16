from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.db.models import Q, Sum
from .models import *

def get_student(request):
    students = Student.objects.all()
    if request.GET.get('search'):
        search = request.GET.get('search')
        students = students.filter(
            Q(department__department__icontains = search) |
            Q(student_name__icontains = search) |
            Q(student_id__student_id__icontains = search) |
            Q(student_email__icontains = search) |
            Q(student_age__icontains = search) 
        )
        paginator = Paginator(students, len(students))
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        return render(request, 'students.html', context={'students_page':page_obj})
    
    paginator = Paginator(students, 15)  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, 'students.html', context={'students_page':page_obj})
