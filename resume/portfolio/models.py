from django.db import models


class Skill(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    link = models.URLField(blank=True)
    image = models.ImageField(upload_to='upload_media/')

    def __str__(self):
        return self.title


class Education(models.Model):
    field_of_study = models.CharField(max_length=100)

    def __str__(self):
        return self.institution


class WorkExperience(models.Model):
    company = models.CharField(max_length=150)
    position = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.position} at {self.company}"
