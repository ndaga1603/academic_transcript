from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Department(models.Model):
    department_id = models.CharField(primary_key=True, max_length=20)
    department_name = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.department_name


class Course(models.Model):
    course_id = models.CharField(primary_key=True, max_length=20)
    course_name = models.CharField(max_length=20)
    department = models.ForeignKey( Department, verbose_name="departiment", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.course_name


class Category(models.Model):
    CATEGORY = (
        ('ORDINARY DIPLOMA', 'OD'),
        ('BACHELOR DEGREE', 'BCH'),
        ('MASTERS', 'MS'),

    )
    id = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(max_length=20, choices=CATEGORY)

    def __str__(self) -> str:
        return self.name



class Student(models.Model):
    GENDER = (
        ('male', 'male'),
        ('female','female')
    )
    registration_number = models.CharField(primary_key=True, max_length=20)
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    form_four_index = models.CharField(max_length=20)
    birthdate = models.DateField()
    gender = models.CharField(max_length=6, choices=GENDER)
    course = models.ForeignKey(Course, verbose_name="course_id", on_delete=models.CASCADE)
    department = models.ForeignKey(Department, verbose_name="departiment_id", on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


    def __str__(self) -> str:
        return self.name.first_name + " " + self.name.last_name


class Enrollment(models.Model):
    student = models.ManyToManyField(Student)
    starting_year = models.DateField()
    enrollment_status = models.CharField(max_length=5)

    def __str__(self) -> str:
        return f"{self.starting_year.year}"


class NTA_Level(models.Model):
    LEVEL = (
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        
    )
    level_id = models.CharField(primary_key=True, max_length=20)
    level = models.CharField(max_length=20, choices=LEVEL)
    number_of_semesters = models.IntegerField(validators=[MaxValueValidator(6), MinValueValidator(2)])

    def __str__(self) -> str:
        return self.level



class Class(models.Model):
    class_id = models.CharField(primary_key=True, max_length=20)
    class_name = models.CharField(max_length=20)
    course = models.ForeignKey(Course, verbose_name="course_id", on_delete=models.CASCADE)
    NTA_level = models.ForeignKey(NTA_Level, verbose_name="NTA_level", on_delete=models.CASCADE)
    starting_year_class = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.class_name

    
class Module(models.Model):
    module_code = models.CharField(primary_key=True, max_length=20)
    module_name = models.CharField(max_length=20)
    module_credit = models.CharField(max_length=20)
  
    def __str__(self) -> str:
        return self.module_name


class Class_Module(models.Model):
    class_module_id = models.CharField(primary_key=True, max_length=20)
    class_id = models.ForeignKey(Class, verbose_name="class", on_delete=models.CASCADE)
    module_code = models.ForeignKey(Module, verbose_name="module_code", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.class_module_id


class HOD(models.Model):
    hod_id = models.CharField(primary_key=True, max_length=20)
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, verbose_name="department_name", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name.first_name + " " + self.name.last_name


class Semester_Student_result(models.Model):
    result_id = models.CharField(primary_key=True, max_length=20)
    academic_year = models.DateField()
    module_code = models.ForeignKey(Module, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, verbose_name="registration_number", on_delete=models.CASCADE)
    CA = models.FloatField()
    FE = models.FloatField()
    status = models.CharField(max_length=15)
    
    def __str__(self) -> str:
        return f"{self.student}  {self.academic_year.year}"


class Overall_result(models.Model):
    result_id = models.CharField(primary_key=True, max_length=20)
    student = models.ForeignKey(Student, verbose_name="registration_number", on_delete=models.CASCADE)
    academic_year = models.DateField()
    nta_level =models.ForeignKey(NTA_Level, on_delete=models.CASCADE)
    GPA = models.FloatField()
    pass_status = models.BooleanField()

    def __str__(self) -> str:
        return f"{self.student} {self.academic_year.year}"

