from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class UserProfile(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    phone = PhoneNumberField(region="RU")
    email = models.EmailField(verbose_name="Почта")
    telegram = models.URLField(blank=True, null=True, verbose_name="Telegram")
    vk = models.URLField(blank=True, null=True, verbose_name="VK")
    image = models.ImageField(upload_to='upload_media/', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Профиль пользователя"
        verbose_name_plural = "Профили пользователей"


class Skill(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(blank=True, verbose_name="Описание")

    class Meta:
        verbose_name = "Навык"
        verbose_name_plural = "Навыки"

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=150, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    link = models.URLField(blank=True, verbose_name="Ссылка")

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"

    def __str__(self):
        return self.title


class ProjectImage(models.Model):
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name="Проект")
    image = models.ImageField(
        upload_to='upload_media/',
        verbose_name="Изображение")

    class Meta:
        verbose_name = "Изображение проекта"
        verbose_name_plural = "Изображения проектов"

    def __str__(self):
        return f"Изображение для {self.project.title}"


class Education(models.Model):
    field_of_study = models.CharField(
        max_length=100,
        verbose_name="Специальность"
        )
    institution = models.CharField(
        max_length=100,
        verbose_name="Учебное заведение",
        default="Не указано"
        )

    class Meta:
        verbose_name = "Образование"
        verbose_name_plural = "Образование"

    def __str__(self):
        return self.institution


class EducationImage(models.Model):
    project = models.ForeignKey(
        Education,
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name="Образование")
    image = models.ImageField(
        upload_to='upload_media/',
        verbose_name="Изображение")

    class Meta:
        verbose_name = "Изображение диплома"
        verbose_name_plural = "Изображения дипломов"

    def __str__(self):
        return f"Изображение для {self.project.field_of_study}"


class WorkExperience(models.Model):
    company = models.CharField(max_length=150, verbose_name="Компания")
    position = models.CharField(max_length=100, verbose_name="Должность")
    description = models.TextField(verbose_name="Описание")
    start_date = models.DateField(verbose_name="Дата начала")
    end_date = models.DateField(
        blank=True,
        null=True,
        verbose_name="Дата окончания"
        )

    class Meta:
        verbose_name = "Опыт работы"
        verbose_name_plural = "Опыт работы"

    def __str__(self):
        return f"{self.position} в {self.company}"
