from django.shortcuts import render

from .models import Project, Education


def home(request):
    return render(request, 'portfolio/home.html')


def skills(request):
    return render(request, 'portfolio/skills.html')


def projects(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/projects.html', {'projects': projects})


def education(request):
    education = Education.objects.all()
    return render(request, 'portfolio/education.html', {'education': education})


def work_experience(request):
    return render(request, 'portfolio/work_experience.html')
