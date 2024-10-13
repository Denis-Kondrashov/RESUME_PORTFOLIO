from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('skills/', views.skills, name='skills'),
    path('projects/', views.achievements, name='projects'),
    path('education/', views.education, name='education'),
    path('work-experience/', views.work_experience, name='work_experience'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
