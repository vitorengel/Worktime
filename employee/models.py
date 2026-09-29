from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    hire_date = models.DateField()
    birthday = models.DateField()
    email = models.EmailField()
    hourly_rate = models.DecimalField(
        decimal_places=2,
        max_digits=10,
    )
    department = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="employees/", blank=True, null=True)
    description = models.TextField(default="")

    def __str__(self):
        return self.name