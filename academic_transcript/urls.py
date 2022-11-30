
from django.contrib import admin
from django.urls import path
from transcript_app.views import HomeView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='index'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
