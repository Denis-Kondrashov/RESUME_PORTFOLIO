from django.shortcuts import render


def new_html(request):
    return render(request, 'portfolio/new_home.html')


def home(request):
    return render(request, 'portfolio/home.html')


def skills(request):
    return render(request, 'portfolio/skills.html')


def achievements(request):
    return render(request, 'portfolio/achievements.html')


def education(request):
    return render(request, 'portfolio/education.html')


def work_experience(request):
    return render(request, 'portfolio/work_experience.html')
