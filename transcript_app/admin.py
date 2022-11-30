from django.contrib import admin
from .models import Student, Semester_Student_result, Department, Class, Class_Module
from .models import Course, Enrollment, Category, Module, HOD, Overall_result, NTA_Level

admin.site.register(Student)
admin.site.register(Enrollment)
admin.site.register(Department)
admin.site.register(Course)
admin.site.register(NTA_Level)
admin.site.register(Class_Module)
admin.site.register(Class)
admin.site.register(Category)
admin.site.register(Module)
admin.site.register(HOD)
admin.site.register(Semester_Student_result)
admin.site.register(Overall_result)
