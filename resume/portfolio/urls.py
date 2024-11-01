from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('skills/', views.SkillsListView.as_view(), name='skills'),
    path('projects/', views.ProjectsListView.as_view(), name='projects'),
    path('education/', views.EducationListView.as_view(), name='education'),
    path('work-experience/',
         views.WorkExperienceListView.as_view(), name='work_experience'),
]
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)#
