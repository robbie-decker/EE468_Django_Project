# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


# class Course(models.Model):
#     course_id = models.CharField(primary_key=True, max_length=8)
#     title = models.CharField(max_length=32, blank=True, null=True)
#     dept_name = models.ForeignKey('Department', models.DO_NOTHING, db_column='dept_name', blank=True, null=True)
#     credits = models.IntegerField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'course'


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


# class Prereq(models.Model):
#     course = models.ForeignKey(Course, models.DO_NOTHING)
#     preq = models.ForeignKey(Course, models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'prereq'
#         unique_together = (('course', 'preq'),)


# class Section(models.Model):
#     course = models.ForeignKey(Course, models.DO_NOTHING)
#     sec_id = models.CharField(max_length=8)
#     semester = models.IntegerField()
#     year = models.IntegerField()
#     building = models.CharField(max_length=8, blank=True, null=True)
#     room = models.CharField(max_length=8, blank=True, null=True)
#     capacity = models.IntegerField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'section'
#         unique_together = (('course', 'sec_id', 'semester', 'year'),)


class Student(models.Model):
    id = models.CharField(primary_key=True, max_length=8)
    name = models.CharField(max_length=20, blank=True, null=True)
    dept_name = models.ForeignKey(Department, models.DO_NOTHING, db_column='dept_name', blank=True, null=True)
    total_credits = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student'


# class Takes(models.Model):
#     id = models.ForeignKey(Student, models.DO_NOTHING, db_column='id')
#     course = models.ForeignKey(Section, models.DO_NOTHING)
#     sec = models.ForeignKey(Section, models.DO_NOTHING)
#     semester = models.ForeignKey(Section, models.DO_NOTHING, db_column='semester')
#     year = models.ForeignKey(Section, models.DO_NOTHING, db_column='year')
#     grade = models.CharField(max_length=8, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'takes'
#         unique_together = (('id', 'course', 'sec', 'semester', 'year'),)


# class Teaches(models.Model):
#     course = models.ForeignKey(Section, models.DO_NOTHING)
#     sec = models.ForeignKey(Section, models.DO_NOTHING)
#     semester = models.ForeignKey(Section, models.DO_NOTHING, db_column='semester')
#     year = models.ForeignKey(Section, models.DO_NOTHING, db_column='year')
#     id = models.ForeignKey(Instructor, models.DO_NOTHING, db_column='id')

#     class Meta:
#         managed = False
#         db_table = 'teaches'
#         unique_together = (('id', 'course', 'sec', 'year', 'semester'),)
