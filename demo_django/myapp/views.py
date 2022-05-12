from django.shortcuts import render
from django.http import HttpResponse

from .models import Instructor, Department, Student
from django.db.models import Avg, Min, Max

# Create your views here.
def index(request):
    department_min_max_avg = Instructor.objects.values("dept").annotate(avg_value=Avg("salary"), min_value=Min("salary"), max_value=Max('salary'))
    # department_avg_salary = Instructor.objects.aggregate(Avg('salary'))
    instructor_names = Instructor.objects.values('name').order_by('name')
    context = {
        'instructor_names' : instructor_names,
        'department_min_max_avg': department_min_max_avg,
    }
    print(f"Here is some stuff: {instructor_names}")
    print(f"Here is some more stuff: {department_min_max_avg}")
    return render(request, 'myapp/index.html', context)
