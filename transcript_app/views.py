from django.views.generic import DetailView, ListView
from .models import Overall_result, Semester_Student_result


class HomeView(ListView):
    template_name = 'index.html'
    model = Overall_result
    paginate_by = 10

class SemesterView(DetailView):
    template_name = 'semester.html'
    model = Semester_Student_result



class TranscriptView(DetailView):
    template_name = 'transcript.html'
    model = Overall_result
   

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        gpa_object = Overall_result.objects.first()
        gpa_value = getattr(gpa_object, 'GPA')

        # calculating award per GPA
        if gpa_value < 2:
            context['gpa_classification'] = "FAIL"
        elif gpa_value < 3.5:
            context['gpa_classification'] = "LOWER CLASS"
        elif gpa_value < 4.5:
            context['gpa_classification'] = "UPPER SECOND CLASS"
        else:
            context['gpa_classification'] = "UPPER FIRST CLASS"
        
        # calculating GPA and grade for each score
        semester_results = Semester_Student_result.objects.first()
        ca = getattr(semester_results, 'CA')
        fe = getattr(semester_results, 'FE')
        level = getattr(semester_results, 'nta_level')
    
     
        sem_1_level_4 = Semester_Student_result.objects.filter(
                semester=1, nta_level__level=4)
        sem_1_level_5 = Semester_Student_result.objects.filter(
            semester=1, nta_level__level=5)
        sem_1_level_6 = Semester_Student_result.objects.filter(
            semester=1, nta_level__level=6)
        sem_1_level_7 = Semester_Student_result.objects.filter(
            semester=1, nta_level__level=7)
        sem_1_level_8 = Semester_Student_result.objects.filter(
            semester=1, nta_level__level=8)

        sem_2_level_4 = Semester_Student_result.objects.filter(
            semester=2, nta_level__level=4)
        sem_2_level_5 = Semester_Student_result.objects.filter(
            semester=2, nta_level__level=5)
        sem_2_level_6 = Semester_Student_result.objects.filter(
            semester=2, nta_level__level=6)
        sem_2_level_7 = Semester_Student_result.objects.filter(
            semester=2, nta_level__level=7)
        sem_2_level_8 = Semester_Student_result.objects.filter(
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

        score = ca + fe
        if int(level.level) <= 5:
            if score >= 80:
                context['grade'] = 'A'

            if 65 <= score <= 79:
                context['grade'] = 'B'

            if 50 <= score <= 64:
                context['grade'] = 'C'

            if 40 <= score <= 49:
                context['grade'] = 'D'

            if score <= 39:
                context['grade'] = 'F'

        if int(level.level) == 6:
            if score >= 75:
                context['grade'] = 'A'

            if 65 <= score <= 74:
                context['grade'] = 'B+'

            if 55 <= score <= 64:
                context['grade'] = 'B'

            if 45 <= score <= 54:
                context['grade'] = 'C'

            if 35 <= score <= 44:
                context['grade'] = 'D'

            if score <= 34:
                context['grade'] = 'F'

        if 7 <= int(level.level) <= 8:

            if score >= 70:
                context['grade'] = 'A'

            if 60 <= score <= 69:
                context['grade'] = 'B+'

            if 50 <= score <= 59:
                context['grade'] = 'B'

            if 40 <= score <= 49:
                context['grade'] = 'C'

            if 30 <= score <= 39:
                context['grade'] = 'D'

            if score <= 30:
                context['grade'] = 'F'


        context['semester_results'] = Semester_Student_result.objects.all()
        return context

  
    
