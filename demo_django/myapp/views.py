from django.shortcuts import render
from django.http import HttpResponse

from .models import Instructor, Department, Student

# Create your views here.
def index(request):
    print(Instructor)
    instructor_names = Instructor.objects.values_list("name")
    context = {
        'instructor_names' : instructor_names,
    }
    print(f"Here is some stuff: {instructor_names}")
    print(instructor_names)
    return render(request, 'myapp/index.html', context)