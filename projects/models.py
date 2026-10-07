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


class Allocation(models.Model):
    employee = models.ForeignKey(
        "employee.Employee",
        on_delete=models.CASCADE,
        related_name="allocations"
    )

    project = models.ForeignKey(
        "Project",
        on_delete=models.CASCADE,
        related_name="allocations"
    )

    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    status = models.CharField(
        max_length=20,
        default="allocated"
    )

    def __str__(self):
        return f"{self.employee.name} - {self.project.project_name} - {self.date}"
    