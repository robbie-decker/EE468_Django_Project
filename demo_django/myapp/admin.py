from django.contrib import admin

# Register your models here.

from .models import Instructor, Department, Student

admin.site.register([Instructor, Department, Student])