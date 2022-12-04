
from django.contrib import admin
from django.urls import path
from transcript_app.views import HomeView, SemesterView, TranscriptView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='index'),
    path('<int:pk>/', TranscriptView.as_view(), name='transcript'),
    path('<int:pk>/', SemesterView.as_view(), name='semester'),

] 
