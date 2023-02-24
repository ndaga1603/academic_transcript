
from django.contrib import admin
from django.urls import path
from transcript_app.views import *
from django.contrib.auth.views import LogoutView, LoginView

# pdf stuff
from django_pdfkit import PDFView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='index'),
    path('studentlist/', StudentView.as_view(), name='studentlist'),
    path('program-class/', ProgramClassView.as_view(), name='program-class'),
    path('departiments/', DepartimentView.as_view(), name='departiments'),
    path('levels/', LevelsView.as_view(), name='levels'),
    path('register/', StudentRegistrationView.as_view(), name='stu-reg'),
    # path('class-module/', CreateClassModules.as_view(), name='class-module'),
    path('module-list/', ModuleList.as_view(), name='module-list'),
    path('class-list/', ClassListView.as_view(), name='class-list'),
    path('class-results/<str:class_id>/',
         ClassResultView.as_view(), name='class-results'),





    path('<int:pk>/', SemesterView.as_view(), name='semester'),
    path('result/<str:registration_number>/', ResultView.as_view(), name='results'),
    path('search/', SearchView.as_view(), name='search'),

    path('logout/', LogoutView.as_view(next_page="login"), name="logout"),
    path('login/', LoginView.as_view(template_name='login.html', next_page='index'), name='login'),

    path('results-pdf/', PDFView.as_view(template_name='results.html'), name='results-pdf')

] 
