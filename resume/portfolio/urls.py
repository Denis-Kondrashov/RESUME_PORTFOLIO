from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('skills/', views.skills, name='skills'),
    path('projects/', views.achievements, name='projects'),
    path('education/', views.education, name='education'),
    path('work-experience/', views.work_experience, name='work_experience'),
]
