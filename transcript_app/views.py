from django.views.generic import DetailView, ListView, TemplateView, CreateView, FormView
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from .models import *
from .forms import *

# from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django_pdfkit import PDFView

# from django.contrib.auth.views import LoginView

# from django.template.loader import render_to_string
# from weasyprint import HTML
# import tempfile


# def pdf(request):
#     response = HttpResponse(content_type="pdf")
#     response['Content-Disposition'] = 'attachment; filename="ndaga".pdf'
#     response['Content-Transfer-Encoding'] = 'binary'

#     html_string = render_to_string('pdf.html')
#     html = HTML(string=html_string)

#     result = html.write_pdf()

#     with tempfile.NamedTemporaryFile(delete=True) as output:
#         output.write(result)
#         output.flush()
#         output = open(output.name, 'rb')
#         response.write(output.read())

#     return response

class SearchView(FormView):
    template_name = 'result-form.html'
    form_class = ResuultForm

    def form_valid(self, form):
        registration_number = form.cleaned_data['registration_number']
        return redirect(reverse('results', kwargs={'registration_number': registration_number}))

class ResultView(PDFView, TemplateView):
    template_name = 'results.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        registration_number = kwargs.get('registration_number')

        if registration_number:
            student = get_object_or_404(Student, registration_number=registration_number)
            context["student"] = student
            semester_results = Student_Semester_Result.objects.filter(student=student)
            overall_results = OverallResult.objects.filter(student=student)
            context['overall_results'] = overall_results

            sem_1_level_4 = Student_Semester_Result.objects.filter(
                    semester=1, nta_level__level=4)
       
            sem_1_level_5 = Student_Semester_Result.objects.filter(
                semester=1, nta_level__level=5)
            sem_1_level_6 = Student_Semester_Result.objects.filter(
                semester=1, nta_level__level=6)
            sem_1_level_7 = Student_Semester_Result.objects.filter(
                semester=1, nta_level__level=7)
            sem_1_level_8 = Student_Semester_Result.objects.filter(
                semester=1, nta_level__level=8)

            sem_2_level_4 = Student_Semester_Result.objects.filter(
                semester=2, nta_level__level=4)
            sem_2_level_5 = Student_Semester_Result.objects.filter(
                semester=2, nta_level__level=5)
            sem_2_level_6 = Student_Semester_Result.objects.filter(
                semester=2, nta_level__level=6)
            sem_2_level_7 = Student_Semester_Result.objects.filter(
                semester=2, nta_level__level=7)
            sem_2_level_8 = Student_Semester_Result.objects.filter(
                semester=2, nta_level__level=8)
            
            context['semester_1_level_4'] = sem_1_level_4
            context['semester_1_level_5'] = sem_1_level_5
            context['semester_1_level_6'] = sem_1_level_6
            context['semester_1_level_7'] = sem_1_level_7
            context['semester_1_level_8'] = sem_1_level_8

            context['semester_2_level_4'] = sem_2_level_4
            context['semester_2_level_5'] = sem_2_level_5
            context['semester_2_level_6'] = sem_2_level_6
            context['semester_2_level_7'] = sem_2_level_7
            context['semester_2_level_8'] = sem_2_level_8


            gpa_value = getattr(overall_results.first(), 'GPA')

            # calculating award per GPA
            if gpa_value < 2:
                context['gpa_classification'] = "FAIL"
            elif gpa_value < 3.5:
                context['gpa_classification'] = "LOWER CLASS"
            elif gpa_value < 4.5:
                context['gpa_classification'] = "UPPER SECOND CLASS"
            else:
                context['gpa_classification'] = "UPPER FIRST CLASS"

        return context
    


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["students"] = Student.objects.all().count()
        context["classes"] = Class.objects.all().count()
        context["programs"] = Program.objects.all().count()

        return context
    
 

class SemesterView(DetailView):
    template_name = 'semester.html'
    model = Student_Semester_Result



class StudentView(ListView):
    template_name = 'studentlist.html'
    model = Student
   

class ProgramClassView(ListView):
    template_name = 'program-class.html'
    model = Program

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Classes"] = Class.objects.all()
        return context
    

class DepartimentView(ListView):
    template_name = 'departiments.html'
    model = Department
      
  
class LevelsView(ListView):
    template_name = 'levels.html'
    model = NTALevel


class StudentRegistrationView(CreateView):
    template_name = 'student-reg.html'
    form_class = StudentRegistrationForm



# class CreateClassModules(CreateView):
#     template_name = 'class-module.html'
#     form_class = ClassModuleForm
#     success_url = reverse_lazy('index')


class ModuleList(ListView):
    template_name = 'all-modules.html'
    model = Module
 

class ClassListView(ListView):
    template_name = 'classlist.html'
    model = Class

# class ClassResultView(TemplateView):
#     template_name = 'class-results.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         _class = kwargs.get('class_id')

#         if _class:
#             results = []
#             students = Student.objects.filter(class_name=_class)
#             print(students)
#             for student in range(len(students)):
#                 semester_results = Student_Semester_Result.objects.filter(
#                     student=students[student])
#                 results.append(semester_results)

#             context["semester_results"] = results
#         return context
            
    
# class ClassResultView(TemplateView):
#     template_name = 'class-results.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         _class = kwargs.get('class_id')

#         if _class:
#             # Get all students in the class
#             students = Student.objects.filter(class_name=_class)

#             # Group semester results by student and then by module
#             student_results = {}
#             for student in students:
#                 semester_results = Student_Semester_Result.objects.filter(
#                     student=student)
#                 for result in semester_results:
#                     if result.student not in student_results:
#                         student_results[result.student] = {}
#                     if result.module_code not in student_results[result.student]:
#                         student_results[result.student][result.module_code] = []
#                     student_results[result.student][result.module_code].append(
#                         result)

#             # Prepare the context with the grouped results
#             context["student_results"] = student_results

#         return context

class ClassResultView(TemplateView):
    template_name = 'class-results.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        _class = kwargs.get('class_id')

        if _class:
            student_results = {}
            students = Student.objects.filter(class_name=_class)
            for student in students:
                semester_results = Student_Semester_Result.objects.filter(
                    student=student)
                student_results[student.registration_number] = semester_results

            sample = student_results['20021098755']
            for s in sample:
                print(s.ca)
            context["students"] = students
            context["student_results"] = student_results

        return context







# class LoginView(LoginView):
#     template_name = 'login.html'

    # def form_valid(self, form):
    #     user = form.get_user()
    #     if user.groups.filter(name='HOD'):
    #         self.next_page = 'index'
    #     elif user.is_supervisor:
    #         self.next_page = 'supervisor'
    #     else:
    #         self.next_page = 'index'

    #     return super().form_valid(form)
