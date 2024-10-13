from django.contrib import admin
from django.utils.html import mark_safe

from .models import Skill, Project, Education, WorkExperience


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    list_filter = ('name',)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'link', 'image', 'image_tag')
    search_fields = ('title', 'description')
    list_filter = ('title',)
    list_editable = ('link',)
    list_per_page = 20

    def image_tag(self, obj):
        if obj.image:
            return mark_safe(
                f'<img src="{obj.image.url}" width="125" height="125" />'
                )
        else:
            return 'No image'
    image_tag.short_description = 'Превью'


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('institution', 'field_of_study')
    search_fields = ('institution', 'field_of_study')
    list_filter = ('institution',)


@admin.register(WorkExperience)
class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = ('company', 'position', 'start_date', 'end_date')
    search_fields = ('company', 'position')
    list_filter = ('company', 'start_date')
    date_hierarchy = 'start_date'
    list_per_page = 20


admin.site.empty_value_display = 'Не задано'
