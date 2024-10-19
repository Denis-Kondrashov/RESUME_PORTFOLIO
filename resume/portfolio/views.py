from django.views.generic import ListView, TemplateView

from .models import Project, Education, Skill, WorkExperience


# def home(request):
#     return render(request, 'portfolio/home.html')

class Home(TemplateView):
    template_name = 'portfolio/home.html'


class SkillsListView(ListView):
    model = Skill
    template_name = 'portfolio/skills.html'
    context_object_name = 'skills'


class ProjectsListView(ListView):
    model = Project
    template_name = 'portfolio/projects.html'
    context_object_name = 'projects'


class EducationListView(ListView):
    model = Education
    template_name = 'portfolio/education.html'
    context_object_name = 'education'


class WorkExperienceListView(ListView):
    model = WorkExperience
    template_name = 'portfolio/work_experience.html'
    context_object_name = 'work_experiences'
