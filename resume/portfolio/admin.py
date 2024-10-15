from django.contrib import admin
from django.utils.html import mark_safe

from .models import (Skill,
                     Project,
                     ProjectImage,
                     EducationImage,
                     Education,
                     WorkExperience
                     )


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    list_filter = ('name',)


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1
    fields = ('image', 'preview')
    readonly_fields = ('preview',)

    def preview(self, obj):
        if obj.image:
            return mark_safe(
                f'<img src="{obj.image.url}" width="100" height="100" />'
                )
        return 'Нет изображения'
    preview.short_description = 'Превью'


class EducationImageInline(admin.TabularInline):
    model = EducationImage
    extra = 1
    fields = ('image', 'preview')
    readonly_fields = ('preview',)

    def preview(self, obj):
        if obj.image:
            return mark_safe(
                f'<img src="{obj.image.url}" width="100" height="100" />'
                )
        return 'Нет изображения'
    preview.short_description = 'Превью'


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'link', 'image_tag')
    search_fields = ('title', 'description')
    list_filter = ('title',)
    list_editable = ('link',)
    list_per_page = 20
    inlines = [ProjectImageInline]

    def image_tag(self, obj):
        images = obj.images.all()[:3]
        if images:
            return mark_safe(
                ''.join(
                    f'<img src="{image.image.url}" width="50" height="50" '
                    f'style="margin-right: 5px;" />' for image in images
                )
            )
        return 'No image'

    image_tag.short_description = 'Превью'


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('institution', 'field_of_study', 'image_tag')
    search_fields = ('institution', 'field_of_study')
    list_filter = ('institution',)
    inlines = [EducationImageInline]

    def image_tag(self, obj):
        images = obj.images.all()[:3]
        if images:
            return mark_safe(
                ''.join(
                    f'<img src="{image.image.url}" width="50" height="50" '
                    f'style="margin-right: 5px;" />' for image in images
                )
            )
        return 'No image'

    image_tag.short_description = 'Превью'


@admin.register(WorkExperience)
class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = ('company', 'position', 'start_date', 'end_date')
    search_fields = ('company', 'position')
    list_filter = ('company', 'start_date')
    date_hierarchy = 'start_date'
    list_per_page = 20


admin.site.empty_value_display = 'Не задано'
