from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('skills/', views.skills, name='skills'),
    path('achievements/', views.achievements, name='achievements'),
    path('education/', views.education, name='education'),
    path('work-experience/', views.work_experience, name='work_experience'),
    path('new_home/', views.new_html, name='new_home'),
]
