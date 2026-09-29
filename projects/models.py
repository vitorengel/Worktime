from django.db import models
from employee.models import Employee

# Create your models here.
class Project(models.Model):
    project_name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    workers = models.ManyToManyField(
        Employee,
        related_name="projects",
        blank=True
    )
    materials = models.TextField()

    def __str__(self):
        return self.project_name
    