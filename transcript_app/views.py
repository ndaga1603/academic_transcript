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
    # context_object_name = "result"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        gpa_object = Overall_result.objects.first()
        gpa_value = getattr(gpa_object, 'GPA')
        if gpa_value < 2:
            context['gpa_classification'] = "FAIL"
        elif gpa_value < 3.5:
            context['gpa_classification'] = "LOWER CLASS"
        elif gpa_value < 4.5:
            context['gpa_classification'] = "UPPER SECOND CLASS"
        else:
            context['gpa_classification'] = "UPPER FIRST CLASS"

        return context
