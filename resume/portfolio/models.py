from django.db import models


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
    image = models.ImageField(
        upload_to='upload_media/',
        verbose_name="Изображение"
        )

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"

    def __str__(self):
        return self.title


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
