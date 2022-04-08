from django.db import models

# Create your models here.

class Department(models.Model):
    dept_name = models.CharField(primary_key=True, max_length=32)
    building = models.CharField(max_length=32, blank=True, null=True)
    budget = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'department'


class Instructor(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=20, blank=True, null=True)
    dept = models.ForeignKey(Department, models.DO_NOTHING, db_column='dept', blank=True, null=True)
    salary = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'instructor'

class Student(models.Model):
    id = models.CharField(primary_key=True, max_length=8)
    name = models.CharField(max_length=20, blank=True, null=True)
    dept_name = models.ForeignKey(Department, models.DO_NOTHING, db_column='dept_name', blank=True, null=True)
    total_credits = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student'
        