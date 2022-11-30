from django.views.generic import TemplateView
from .models import Overall_result


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['results'] = Overall_result.objects.all()
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
