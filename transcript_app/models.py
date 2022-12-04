from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator


class Department(models.Model):
    department_id = models.CharField(primary_key=True, max_length=20)
    department_name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.department_name


class Course(models.Model):
    course_id = models.CharField(primary_key=True, max_length=20)
    course_name = models.CharField(max_length=50)
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
    name = models.CharField(max_length=50, choices=CATEGORY)

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
    course = models.ForeignKey(Course, verbose_name="course", on_delete=models.CASCADE)
    department = models.ForeignKey(Department, verbose_name="belongs to (departiment)", on_delete=models.CASCADE)
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
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    number_of_semesters = models.IntegerField(validators=[MaxValueValidator(6), MinValueValidator(2)])

    def __str__(self) -> str:
        return self.level


class Class(models.Model):
    class_id = models.CharField(primary_key=True, max_length=20)
    class_name = models.CharField(max_length=50)
    course = models.ForeignKey(Course, verbose_name="course", on_delete=models.CASCADE)
    NTA_level = models.ForeignKey(NTA_Level, verbose_name="NTA_level", on_delete=models.CASCADE)
    starting_year_class = models.DateField()

    def __str__(self) -> str:
        return self.class_name

class Module(models.Model):
    module_code = models.CharField(primary_key=True, max_length=20)
    module_name = models.CharField(max_length=50)
    department = models.ForeignKey(Department,verbose_name="belongs to (department)", on_delete=models.CASCADE)
    module_credit = models.CharField(max_length=20)
  
    def __str__(self) -> str:
        return self.module_name


class Class_Module(models.Model):
    class_module_id = models.CharField(primary_key=True, max_length=20)
    class_id = models.ForeignKey(Class, verbose_name="class", on_delete=models.CASCADE)
    module_code = models.ManyToManyField(Module, verbose_name="modules")

    def __str__(self) -> str:
        return self.class_module_id


class HOD(models.Model):
    hod_id = models.CharField(primary_key=True, max_length=20)
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, verbose_name="department name", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name.first_name + " " + self.name.last_name


class Semester_Student_result(models.Model):
    STATUS = (
        ('pass', 'pass'),
        ('fail', 'fail')
    )
    SEMESTER = (
        ('1', 'first semester'),
        ('2', 'second semester')
    )
    student = models.ForeignKey(Student, verbose_name="student name", on_delete=models.CASCADE)
    nta_level = models.ForeignKey(NTA_Level, verbose_name="NTA Level", on_delete=models.CASCADE)
    academic_year = models.CharField(max_length=10)
    semester = models.CharField(max_length=1, choices=SEMESTER)
    module_code = models.ForeignKey(Module, on_delete=models.CASCADE)
    CA = models.FloatField()
    FE = models.FloatField()
    status = models.CharField(max_length=5, choices=STATUS)
    
    def __str__(self) -> str:
        return f"{self.student}  {self.academic_year} {self.semester}"

    def get_absolute_url(self):
        return reverse("semester", kwargs={"pk": self.id})


class Overall_result(models.Model):
    student = models.ForeignKey(Student, verbose_name="registration_number", on_delete=models.CASCADE)
    academic_year = models.CharField(max_length=10)
    nta_level =models.ForeignKey(NTA_Level, on_delete=models.CASCADE)
    GPA = models.FloatField()
    pass_status = models.BooleanField()

    def __str__(self) -> str:
        return f"{self.student} {self.academic_year}"

    def get_absolute_url(self):
        return reverse("transcript", kwargs={"pk": self.id})
    

