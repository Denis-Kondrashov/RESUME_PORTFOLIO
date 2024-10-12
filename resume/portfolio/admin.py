from django.contrib import admin

from .models import Skill, Project, Education, WorkExperience

admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(Education)
admin.site.register(WorkExperience)