from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import AbstractUser
   

class HOD(models.Model):
    hod_id = models.CharField(primary_key=True, max_length=20)
    name = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name.first_name + " " + self.name.last_name


class Department(models.Model):
    department_id = models.CharField(primary_key=True, max_length=20)
    department_name = models.CharField(max_length=50)
    hod = models.OneToOneField(HOD, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.department_name


class Program(models.Model):
    program_id = models.CharField(primary_key=True, max_length=20)
    program_name = models.CharField(max_length=50)
    department = models.ForeignKey( Department, verbose_name="departiment", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.program_id} - {self.program_name}"



class NTALevel(models.Model):
    LEVEL = (
        ('4', 'Basic Technician Certificate'),
        ('5', 'Technician Certificate'),
        ('6', 'Ordinary Diploma'),
        ('7', 'Higher National Diploma'),
        ('8', 'Bachelor Degree'),
        ('9', 'Masters'),
    )

    level_id = models.CharField(primary_key=True, max_length=20)
    level = models.CharField(max_length=20, choices=LEVEL)
    number_of_semesters = models.IntegerField(validators=[MaxValueValidator(6), MinValueValidator(2)])

    def __str__(self) -> str:
        return self.level


class Module(models.Model):
    module_code = models.CharField(primary_key=True, max_length=20)
    module_name = models.CharField(max_length=50)
    departiment = models.ForeignKey(
        Department, verbose_name="belongs to (department)", on_delete=models.CASCADE)
    module_credit = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.module_name
    

class Class(models.Model):
    class_id = models.CharField(primary_key=True, max_length=20)
    class_name = models.CharField(max_length=50)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    # nta_level = models.ForeignKey(NTALevel, verbose_name="level", on_delete=models.CASCADE)
    starting_year = models.DateField()
    modules = models.ManyToManyField(Module)

    def __str__(self) -> str:
        return self.class_name


# class Class_Module(models.Model):
#     class_module_id = models.CharField(primary_key=True, max_length=20)
#     class_id = models.ForeignKey(Class, verbose_name="class", on_delete=models.CASCADE)
#     module_code = models.ManyToManyField(Module, verbose_name="modules")

#     def __str__(self) -> str:
#         return self.class_module_id


class Student(models.Model):
    GENDER = (
        ('male', 'male'),
        ('female', 'female')
    )
    registration_number = models.CharField(primary_key=True, max_length=20)
    first_name = models.CharField(max_length=50, verbose_name="First Name")
    middle_name = models.CharField(max_length=50, verbose_name="Middle Name")
    last_name = models.CharField(max_length=50, verbose_name="Last Name")
    email = models.EmailField(verbose_name="Email address")
    phone_number = models.CharField(max_length=10)
    birthdate = models.DateField()
    gender = models.CharField(max_length=6, choices=GENDER)
    # program = models.ForeignKey(Program, on_delete=models.CASCADE)
    class_name = models.ForeignKey(
        Class, verbose_name='class', on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)


    def __str__(self) -> str:
        return self.first_name + " " + self.last_name


class Enrollment(models.Model):
    student = models.ManyToManyField(Student)
    starting_year = models.DateField()
    enrollment_status = models.CharField(max_length=5)

    def __str__(self) -> str:
        return f"{self.starting_year.year}"
    

class Student_Semester_Result(models.Model):
    STATUS = (
        ('pass', 'pass'),
        ('fail', 'fail')
    )
    SEMESTER = (
        ('1', 'first semester'),
        ('2', 'second semester')
    )
    student = models.ForeignKey(Student, verbose_name="student name", on_delete=models.CASCADE)
    nta_level = models.ForeignKey(NTALevel, verbose_name="NTA Level", on_delete=models.CASCADE)
    academic_year = models.CharField(max_length=10)
    semester = models.CharField(max_length=1, choices=SEMESTER)
    module_code = models.ForeignKey(Module, on_delete=models.CASCADE)
    ca = models.FloatField()
    fe = models.FloatField()
    total = models.FloatField(null=True)
    grade = models.CharField(max_length=1, null=True)

    status = models.CharField(max_length=5, choices=STATUS)
    
    
    def __str__(self) -> str:
        return f"{self.student}  {self.academic_year} {self.semester}"

    def get_absolute_url(self):
        return reverse("semester", kwargs={"pk": self.id})


class OverallResult(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    academic_year = models.CharField(max_length=10)
    nta_level =models.ForeignKey(NTALevel, on_delete=models.CASCADE)
    GPA = models.FloatField()
    pass_status = models.BooleanField()

    def __str__(self) -> str:
        return f"{self.student}  {self.academic_year}"

    def get_absolute_url(self):
        return reverse("transcript", kwargs={"pk": self.id})
    
